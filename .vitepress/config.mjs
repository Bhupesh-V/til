import { defineConfig } from 'vitepress'
import { sidebar } from './sidebar.js'
import { execSync } from 'child_process'
import path from 'path'
import fs from 'fs'

function getGitCreationDate(filePath) {
  try {
    // Extract file name from path
    const fileName = path.basename(filePath);
    
    // Use case-insensitive search for the file name
    const cmd = `git log --diff-filter=A --format=%at -- "*${fileName}"`
    const timestamp = execSync(cmd, { encoding: 'utf-8' }).trim();
    
    // Convert git timestamp to Date
    return new Date(parseInt(timestamp) * 1000);
  } catch (e) {
    console.error(`Failed to get git creation date for ${filePath}:`, e);
    return null;
  }
}

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
      text: 'Laste updated',
      formatOptions: {
        dateStyle: 'medium',
      }
    }
  },
  cleanUrls: true,
  lastUpdated: true,
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

    // Get absolute path
    const filePath = path.resolve(process.cwd(), relativePath)

    if (!fs.existsSync(filePath)) {
      console.log('File not found:', filePath)
      return
    }

    try {
      const createdAt = getGitCreationDate(filePath)
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
  }
})
