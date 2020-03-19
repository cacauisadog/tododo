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
  }
}
