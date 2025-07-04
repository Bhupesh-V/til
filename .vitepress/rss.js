import { Feed } from 'feed'
import { writeFileSync, readFileSync } from 'fs'
import { resolve } from 'path'
import { sidebar } from './sidebar.js'
import { getGitFileCreationDate } from './git.js'
import { createMarkdownRenderer } from 'vitepress'

export async function generateRSSFeed(config) {
  const md = await createMarkdownRenderer(process.cwd())

  const feed = new Feed({
    title: "Bhupesh's TIL",
    description: "Personal Wiki of Interesting things I learn every day at the intersection of career, life & stuff aka my second brain 🧠️",
    id: 'https://til.bhupesh.me/',
    link: 'https://til.bhupesh.me/',
    language: 'en',
    image: 'https://til.bhupesh.me/favicon.png',
    favicon: 'https://til.bhupesh.me/favicon.png',
    feedLinks: {
      rss: 'https://til.bhupesh.me/feed.xml',
      atom: 'https://til.bhupesh.me/atom.xml'
    },
    author: {
      name: 'Bhupesh Varshney',
      link: 'https://bhupesh.me'
    }
  })

  const allPosts = []

  for (const category of sidebar) {
    for (const item of category.items) {
      const filePath = `${item.link}.md`.replace(/^\//, '')
      const absPath = resolve(process.cwd(), filePath)

      let content = ''
      try {
        const rawMd = readFileSync(absPath, 'utf-8')
        const stripped = rawMd.replace(/^---[\s\S]*?---/, '').trim()
        content = md.render(stripped)
      } catch (err) {
        console.warn(`Failed to read/parse ${filePath}:`, err)
      }

      const creationDate = getGitFileCreationDate(filePath)

      allPosts.push({
        title: item.text,
        id: `https://til.bhupesh.me${item.link}`,
        link: `https://til.bhupesh.me${item.link}`,
        category: [{ name: category.text }],
        date: creationDate,
        author: [{ name: 'Bhupesh Varshney', link: 'https://bhupesh.me' }],
        content // <- injected HTML
      })
    }
  }

  allPosts
    .sort((a, b) => b.date.getTime() - a.date.getTime())
    .slice(0, 10)
    .forEach(post => feed.addItem(post))

  const outDir = resolve(config.outDir || '.vitepress/dist')
  writeFileSync(resolve(outDir, 'feed.xml'), feed.rss2())
  writeFileSync(resolve(outDir, 'atom.xml'), feed.atom1())

  console.log('✅ RSS feeds generated using VitePress markdown renderer')
}
