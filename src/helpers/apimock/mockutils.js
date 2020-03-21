export function mockasync(data) {
  data = JSON.parse(JSON.stringify(data))
  return new Promise(resolve => {
    setTimeout(() => resolve({ data: data }), 300)
  })
}
