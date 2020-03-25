import { mockasync } from './mockutils'
import { mockuser } from './db_people'

const luffy = mockuser(true)

export default {
  whoami () {
    return mockasync(luffy).then(response => response.data)
  },
  signup (user) {
    if (user.email === 'da@pau.com') {
      return mockasync({ error: 'Email already in use!' }).then(response => response.data)
    } else {
      return mockasync(luffy).then(response => response.data)
    }
  },
  login (user) {
    if (user.password === 'dapau') {
      return mockasync({ error: 'Invalid email or password!' }).then(response => response.data)
    } else if (user.password) {
      return mockasync(luffy).then(response => response.data)
    }
  },
  logout () {
    return mockasync({}).then(response => response.data)
  }
}