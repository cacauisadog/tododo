<template>
  <div>
    <h2>Account information</h2>
    <p>Username: {{ currentUser.username }}</p>
    <p>Email: {{ currentUser.email }}</p>
    <input
      type="button"
      value="Logout"
      @click="logout()"
    >
  </div>
</template>

<script>
import api from '~api'

export default {
  name: 'AccountInfo',
  computed: {
    currentUser () {
      return this.$store.state.currentUser
    }
  },
  methods: {
    logout () {
      api.auth.logout().then(() => {
        this.$store.commit('removeCurrentUser')
      })
    }
  }
}
</script>

<style></style>
