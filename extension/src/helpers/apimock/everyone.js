import { mockasync } from './mockutils'
import { todoLists } from './db_todolists'

export default {
  getTodoLists () {
    return mockasync(todoLists).then(response => response.data)
  },
  addNewTodo (newTodo) {
    if (newTodo.text === 'kaboom') {
      return mockasync({ error: 'addNewTodo() goes boom!' }).then(
        response => response.data
      )
    }
    newTodo.id = Math.random() * 10
    return mockasync(newTodo).then(response => response.data)
  },
  removeTodo (todo) {
    return mockasync(todo).then(response => response.data)
  }
}
