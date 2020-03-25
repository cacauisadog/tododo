import axios from 'axios'

export function get (url, params) {
  try {
    return axios.get(url, { params: params })
  } catch (ex) {
    console.log(`error in axios.get ${ex.toString()}`)
    throw ex
  }
}

export function post (url, params, config) {
  var fd = new FormData()
  params = params || {}
  Object.keys(params).map(k => {
    fd.append(k, params[k])
  })
  try {
    return axios.post(url, fd, config)
  } catch (ex) {
    console.log(`error in axios.post ${ex.toString()}`)
    throw ex
  }
}