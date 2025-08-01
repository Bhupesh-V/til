import { defineConfig } from 'vitepress'
import { sidebar } from './sidebar.js'
import { generateRSSFeed } from './rss.js'
import { getGitFileCreationDate } from './git.js'
import path from 'path'
import fs from 'fs'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  // base: '/til/',
  title: "Bhupesh's TIL",
  description: "Personal Wiki of Interesting things I learn every day at the intersection of career, life & stuff aka my second brain 🧠️",
  sitemap: {
    hostname: 'https://til.bhupesh.me'
  },
  head: [
    ['link', { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon.png" }],
    ['link', { rel: "alternate", type: "application/rss+xml", title: "RSS Feed", href: "/feed.xml" }],
    ['link', { rel: "alternate", type: "application/atom+xml", title: "Atom Feed", href: "/atom.xml" }],
    ['script', { src: 'https://www.googletagmanager.com/gtag/js?id=G-7M5P7006XV' }],
    ['script', {}, ` window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-7M5P7006XV');`]
  ],
  appearance: {
    initialValue: 'light'
  },
  themeConfig: {
    logo: '/favicon.png',
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      // { text: 'Home', link: '/' },
      {
        component: 'HighlightedLink',
        props: {
          text: 'Work with me!',
          link: 'https://bhupesh.me/hire',
        },
      },
      // { text: 'Work with me!', link: 'https://bhupesh.me/hire' },
      { text: 'Blog', link: 'https://bhupesh.me' },
      { text: 'Bookshelf', link: 'https://bookshelf.bhupesh.me/' },
      { text: 'RSS', link: '/feed.xml' },
    ],

    sidebar: sidebar,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/bhupesh-v' },
      { icon: 'x', link: 'https://x.com/bhupeshimself' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/bhupesh-v' },
    ],

    footer: {
      message: 'Written while 🤔 & 🙇🏽‍♂️ & 🧐<br><i><b>Need a nerdy, research oriented tech writer for your dev tools? <a target="_blank" href="https://bhupesh.me/hire/#domain-b-as-a-technical-writer">Maybe, I can help!</a></b></i>',
    },

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: "Search knowledge base",
                buttonAriaLabel: "Search knowledge base",
              },
            }
          }
        }
      },
    },

    lastUpdated: {
      text: 'Last updated',
      formatOptions: {
        dateStyle: 'medium',
      }
    }
  },
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,
  markdown: {
    config(md) {
      // Add a hook to process the markdown content
      const render = md.render
      md.render = (...args) => {
        const html = render.call(md, ...args)
        return `<PostDate />\n${html}`
      }
    },
  },
  transformPageData(pageData) {
    const relativePath = pageData.relativePath

    if (!relativePath) {
      console.log('No relative path found for page')
      return
    }

    // Ignore file creation date for index.md
    if (relativePath === 'index.md') {
      // console.log('Ignoring file creation date for index.md')
      return
    }

    // Get absolute path
    const filePath = path.resolve(process.cwd(), relativePath)

    if (!fs.existsSync(filePath)) {
      console.log('File not found:', filePath)
      return
    }

    try {
      const createdAt = getGitFileCreationDate(filePath)
      if (!createdAt) {
        return
      }
      // Ensure frontmatter exists
      pageData.frontmatter = pageData.frontmatter || {}

      // Add both timestamp and formatted date
      pageData.frontmatter.createdAt = createdAt
      pageData.frontmatter.createdAtFormatted = createdAt.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })

      // Debug log
      // console.log('Updated frontmatter:', pageData.frontmatter)
    } catch (error) {
      console.error('Error processing', relativePath, ':', error)
    }
  },
  buildEnd: async (config) => {
    generateRSSFeed(config)
  },
})
