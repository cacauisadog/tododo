import { get, post } from './ajaxutils'

export default {
  whoami () {
    return get('/api/whoami').then(
      response => response.data)
  },
  signup (user) {
    return post('/api/signup', { user: JSON.stringify(user) }).then(
      response => response.data
    )
  },
  login (user) {
    return post('/api/login', { user: JSON.stringify(user) }).then(
      response => response.data
    )
  },
  logout () {
    return post('/api/logout').then(
      response => response.data
    )
  }
}