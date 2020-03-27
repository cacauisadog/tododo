<template>
  <div>
    <h1>tododo</h1>
    <p v-if="loading">
      loading :)
    </p>
    <div v-else>
      <div
        v-if="todoLists && todoLists.length > 0"
        class="todolists"
      >
        <todo-list
          v-for="todoList in todoLists"
          :key="todoList.id"
          :title="todoList.title"
          :todos="todoList.todos"
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
    }
  }
}
</script>

<style lang="scss" scoped>
p,
input {
  margin: 0;
}

.todolists {
  display: grid;
  grid-gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  margin: auto;
  max-width: 100%;
  padding: 20px;
}
</style>
