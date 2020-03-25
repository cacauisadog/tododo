<template>
  <div>
    <h1>Already have an account?</h1>
    <hr>
    <form @submit.prevent="login()">
      <label for="email">Email:</label>
      <br>
      <input
        id="email"
        v-model="user.email"
        type="email"
        name="email"
      >
      <br>
      <label for="password">Password:</label>
      <br>
      <input
        id="password"
        v-model="user.password"
        type="password"
        name="password"
      >
      <br>
      <button type="submit">
        Login
      </button>
    </form>
    <pre>{{ loggedUser }}</pre>
    <p
      v-if="error"
      style="color: red;"
    >
      {{ error }}
    </p>
  </div>
</template>

<script>
import api from '~api'

export default {
  name: 'LoginForm',
  data () {
    return {
      user: {
        email: '',
        password: ''
      },
      error: null
    }
  },
  computed: {
    loggedUser () {
      return this.$store.getters.logged_user
    }
  },
  methods: {
    login () {
      api.auth.login(this.user).then(response => {
        if (response.error) {
          this.error = response.error
        } else {
          this.$store.commit('setCurrentUser', response)
        }
      })
    }
  }
}
</script>

<style></style>
