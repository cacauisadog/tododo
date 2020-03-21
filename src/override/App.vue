<template>
  <div>
    <h1>tododo</h1>
    <p v-if="loading">loading :)</p>
    <div v-else-if="todoList && todoList.length > 0" class="margin-bottom">
      <todo-item
        v-for="todo in todoList"
        :key="todo.id"
        :item="todo"
        @removeTodo="removeTodo($event)"
      />
    </div>
    <p v-else class="margin-bottom">please add a todo</p>

    <form @submit.prevent>
      <input type="text" name="todoText" v-model="newTodoText" />
      <button type="submit" @click="addNewTodo()">+</button>
    </form>
    <p v-if="loadingTodo">todo action loading!</p>
  </div>
</template>

<script>
import api from '~api'
import TodoItem from '@/components/TodoItem.vue'

export default {
  name: 'App',
  components: { TodoItem },
  created() {
    api.everyone.getTodos().then(result => {
      this.todoList = result.todoList
      this.loading = false
    })
  },
  data() {
    return {
      loading: true,
      loadingTodo: false,
      todoList: undefined,
      newTodoText: ''
    }
  },
  methods: {
    addNewTodo() {
      if (this.newTodoText === '') return
      this.loadingTodo = true
      const newTodo = {
        text: this.newTodoText,
        isDone: false
      }
      api.everyone
        .addNewTodo(newTodo)
        .then(newTodo => {
          if (newTodo.error) {
            console.log(newTodo.error)
          } else {
            this.todoList.push(newTodo)
            this.newTodoText = ''
          }
        })
        .finally(() => {
          this.loadingTodo = false
        })
    },
    removeTodo(todo) {
      this.loadingTodo = true
      api.everyone
        .removeTodo(todo.id)
        .then(response => {
          if (response.error) {
            console.log(response.error)
          } else {
            const todoIndex = this.todoList.indexOf(todo)
            this.todoList.splice(todoIndex, 1)
          }
        })
        .finally(() => {
          this.loadingTodo = false
        })
    }
  }
}
</script>

<style>
p,
input {
  margin: 0;
}

.margin-bottom {
  margin-bottom: 10px;
}
</style>
