export const mockuser = (keepLoggedIn) => {
  return {
    id: 1,
    username: 'Monkey D. Luffy',
    email: 'luffy@newworld.pr',
    is_active: true,
    is_authenticated: keepLoggedIn
  }
}