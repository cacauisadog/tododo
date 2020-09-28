module.exports = {
  root: true,
  env: {
    node: true,
    webextensions: true
  },
  extends: ['plugin:vue/recommended'],
  plugins: ['vue'],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    quotes: [2, 'single'],
    semi: [2, 'never']
  }
}
