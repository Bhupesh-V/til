import { defineConfig } from 'vitepress'
import { sidebar } from './sidebar.js'

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
      message: 'Written while 🤔 & 🙇🏽‍♂️ & 🧐<br><i>Need a <a target="_blank" href="https://bhupesh.me/hire/#domain-b-as-a-technical-writer">technical writer</a> for your dev tools? Maybe I can help!</i>',
    },

    search: {
      provider: 'local'
    },
  },
  cleanUrls: true,
  lastUpdated: true
})
