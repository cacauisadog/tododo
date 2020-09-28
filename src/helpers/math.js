export function generateRandomCode() {
  const keys = 'abcdefghijklmnopqrstubwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  let code = ''

  for (let i = 0; i < 6; i++) {
    code += keys.charAt(Math.floor(Math.random() * keys.length))
  }

  return code
}