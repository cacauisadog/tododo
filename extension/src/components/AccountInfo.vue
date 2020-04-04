<template>
  <div>
    <h3>Account information</h3>
    <p class="fs-s">
      Username: {{ currentUser.username }}
    </p>
    <p class="fs-s">
      Email: {{ currentUser.email }}
    </p>
    <input
      class="fs-s"
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
