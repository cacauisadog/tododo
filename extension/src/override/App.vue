<template>
  <div>
    <h1>tododo</h1>
    <p v-if="loading">
      loading :)
    </p>
    <div
      v-else
      class="mt-4"
    >
      <button @click="addNewTodoList()">
        <p>New todo list</p>
      </button>
      <div
        v-if="todoLists && todoLists.length > 0"
        class="todolists ma-4"
      >
        <todo-list
          v-for="todoList in todoLists"
          :key="todoList.id"
          :todo-list="todoList"
        />
      </div>
      <hr>
      <div v-if="!currentUser">
        <signup-form />
        <login-form />
      </div>
      <account-info v-else />
    </div>
  </div>
</template>

<script>
import api from '~api'
import SignupForm from '@/components/SignupForm.vue'
import LoginForm from '@/components/LoginForm.vue'
import AccountInfo from '@/components/AccountInfo.vue'
import TodoList from '@/components/TodoList.vue'

export default {
  name: 'App',
  components: {
    SignupForm,
    LoginForm,
    AccountInfo,
    TodoList
  },
  data () {
    return {
      loading: true,
      todoLists: undefined
    }
  },
  computed: {
    currentUser () {
      return this.$store.state.currentUser
    }
  },
  mounted () {
    window.api = api
    this.init()
  },
  methods: {
    init () {
      this.$store.dispatch('whoami').then(() => {
        if (this.currentUser) {
          this.getTodoLists(this.currentUser.id)
        }
      }).finally(() => {
        this.loading = false
      })
    },
    getTodoLists (user_id) {
      api.everyone.getTodoLists(user_id).then(todoLists => {
        if (todoLists.error) {
          console.log(todoLists.error)
        } else {
          this.todoLists = todoLists
        }
      })
    },
    addNewTodoList () {
      api.everyone.addNewTodoList(this.currentUser.id).then(newTodoList => {
        if (newTodoList.error) {
          console.log(newTodoList.error)
        } else {
          this.todoLists.push(newTodoList)
        }
      })
    }
  }
}
</script>

<style lang="scss">
@import "@/assets/css/main.scss";

.todolists {
  display: grid;
  grid-gap: 10px;
  grid-template-columns: repeat(auto-fit, 300px);
  margin: auto;
  max-width: 100%;
}
</style>
