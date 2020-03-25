import { get, post } from './ajaxutils'

export default {
  whoami () {
    return get('http://localhost:5000/api/whoami').then(
      response => response.data)
  },
  signup (user) {
    return post('http://localhost:5000/api/signup', { user: JSON.stringify(user) }).then(
      response => response.data
    )
  },
  login (user) {
    return post('http://localhost:5000/api/login', { user: JSON.stringify(user) }).then(
      response => response.data
    )
  },
  logout () {
    return post('http://localhost:5000/api/logout').then(
      response => response.data
    )
  }
}