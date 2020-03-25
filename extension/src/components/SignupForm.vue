<template>
  <div>
    <h1>New user? Signup here!</h1>
    <hr>
    <form @submit.prevent="signup()">
      <label for="username">Username:</label>
      <br>
      <input
        id="username"
        v-model="user.username"
        type="text"
        name="username"
      >
      <br>
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
        Register
      </button>
    </form>
    <pre v-if="registeredUser">{{ registeredUser }}</pre>
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
  name: 'SignupForm',
  data () {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      },
      registeredUser: null,
      error: null
    }
  },
  methods: {
    signup () {
      api.auth.signup(this.user).then(response => {
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

<style>
</style>