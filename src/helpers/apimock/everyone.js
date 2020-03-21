import { mockasync } from './mockutils'
import { todoList } from './db_todo'

export default {
  getTodos() {
    return mockasync(todoList).then(response => response.data)
  },
  addNewTodo(newTodo) {
    newTodo.id = Math.random() * 10
    return mockasync(newTodo).then(response => response.data)
  }
}
