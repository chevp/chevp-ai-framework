// @ts-check
// Docusaurus config for the chevp-ai-framework Lab.
// Source lives in context/lab/. Builds into ../../docs/flow/ — served as a
// subpath of the existing GitHub Pages site.

const {themes: prismThemes} = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'chevp-ai-framework — Lab',
  tagline: 'Experimental Docusaurus subsite for plans, ADRs, and framework docs',
  favicon: 'img/favicon.ico',

  url: 'https://chevp.github.io',
  baseUrl: '/chevp-ai-framework/flow/',

  organizationName: 'chevp',
  projectName: 'chevp-ai-framework',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  trailingSlash: true,

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/chevp/chevp-ai-framework/edit/main/context/lab/',
          showLastUpdateAuthor: false,
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'chevp-ai-framework Lab',
        logo: {
          alt: 'chevp-ai-framework',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'mainSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://chevp.github.io/chevp-ai-framework/',
            label: 'Main site',
            position: 'right',
          },
          {
            href: 'https://github.com/chevp/chevp-ai-framework',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} Patrice Chevillat. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

module.exports = config;
