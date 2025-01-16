import { defineConfig } from 'vitepress'
import { createContentLoader } from 'vitepress'
import { sidebar } from './sidebar.js'
// https://vitepress.dev/reference/site-config
export default defineConfig({
  // base: '/til/',
  title: "Today I Learned",
  description: "Personal Wiki of Interesting things I learn every day at the intersection of software, life & stuff a.k.a my second brain 🧠️",
  sitemap: {
    hostname: 'https://til.bhupesh.me'
  },
  // head: [
  //   ['link', { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon.png" }],
  //   ['script', { src: 'https://www.googletagmanager.com/gtag/js?id=G-7M5P7006XV' }],
  //   ['script', {}, ` window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-7M5P7006XV');`]
  // ],
  async transformHead({ pageData }) {
    const head = [];

    head.push(['link', { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon.png" }]);
    head.push(['script', { src: 'https://www.googletagmanager.com/gtag/js?id=G-7M5P7006XV' }]);
    head.push(['script', {}, ` window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-7M5P7006XV');`]);

    if (pageData && pageData.frontmatter) {
      if (pageData.frontmatter.description) {
        head.push(['meta', { property: 'og:description', content: pageData.frontmatter.description }]);
      } else {
        try {
          // Create a content loader for the current page
          const content = await createContentLoader(pageData.relativePath, {
            excerpt: true,
            render: true
          }).load();

          // Get the first item if it exists
          const pageContent = content[0];

          // Use excerpt, rendered content, or fallback to title
          const description = pageContent?.excerpt ||
            (pageContent?.html ? pageContent.html.replace(/<[^>]*>/g, '').slice(0, 160) + '...' : '') ||
            pageData.title ||
            'Today I Learned';

          head.push(['meta', { property: 'og:description', content: description }]);
        } catch (error) {
          // Fallback to title if content loading fails
          head.push(['meta', { property: 'og:description', content: pageData.title || 'Today I Learned' }]);
        }
      }
    }

    return head;
  },
  themeConfig: {
    logo: '/favicon.png',
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      // { text: 'Home', link: '/' },
      { text: 'Work with me!', link: 'https://bhupesh.me/hire' },
      { text: 'Blog', link: 'https://bhupesh.me' },
      { text: 'Bookshelf', link: 'https://bookshelf.bhupesh.me/' },
    ],

    sidebar: sidebar,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/bhupesh-v' },
      { icon: 'x', link: 'https://x.com/bhupeshimself' },
    ],

    footer: {
      message: 'Written while 🙇🏽‍♀️',
    },

    search: {
      provider: 'local'
    },
  },
  cleanUrls: true,
})
