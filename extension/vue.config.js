const path = require('path')

const _isdev = process.env.npm_lifecycle_event === 'dev'
const _apimock =
  process.env.API_MOCK === '1' || (process.env.API_MOCK === undefined && _isdev)
const _apijs = _apimock ? 'apimock' : 'api'

module.exports = {
  pages: {
    options: {
      template: 'public/browser-extension.html',
      entry: './src/options/main.js',
      title: 'Options'
    },
    override: {
      template: 'public/browser-extension.html',
      entry: './src/override/main.js',
      title: 'tododo - New Tab'
    }
  },
  pluginOptions: {
    browserExtension: {
      componentOptions: {}
    }
  },
  configureWebpack: {
    resolve: {
      alias: { '~api': path.resolve(__dirname, `src/helpers/${_apijs}`) }
    }
  }
}
