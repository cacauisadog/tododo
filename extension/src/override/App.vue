<template>
  <div>
    <h1>tododo</h1>
    <p v-if="loading">
      loading :)
    </p>
    <div
      v-else-if="todoList && todoList.length > 0"
      class="margin-bottom"
    >
      <todo-item
        v-for="todo in todoList"
        :key="todo.id"
        :item="todo"
        @removeTodo="removeTodo($event)"
      />
    </div>
    <p
      v-else
      class="margin-bottom"
    >
      please add a todo
    </p>

    <form @submit.prevent="addNewTodo()">
      <input
        v-model="newTodoText"
        type="text"
        name="todoText"
      >
      <button type="submit">
        +
      </button>
    </form>
    <p v-if="loadingTodo">
      todo action loading!
    </p>

    <div v-if="!currentUser">
      <signup-form />
      <login-form />
    </div>
    <account-info v-else />
  </div>
</template>

<script>
import api from '~api'
import TodoItem from '@/components/TodoItem.vue'
import SignupForm from '@/components/SignupForm.vue'
import LoginForm from '@/components/LoginForm.vue'
import AccountInfo from '@/components/AccountInfo.vue'

export default {
  name: 'App',
  components: {
    TodoItem,
    SignupForm,
    LoginForm,
    AccountInfo
  },
  data () {
    return {
      loading: true,
      loadingTodo: false,
      todoList: undefined,
      newTodoText: ''
    }
  },
  computed: {
    currentUser () {
      return this.$store.state.currentUser
    }
  },
  beforeCreate () {
    this.$store.dispatch('whoami')
  },
  mounted () {
    window.api = api
  },
  methods: {
    addNewTodo () {
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
    removeTodo (todo) {
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
