<template>
  <div class="flex">
    <p :class="{ 'text-linethrough': item.isDone }">{{ item.text }}</p>
    <input class="isDoneCheckbox" type="checkbox" v-model="item.isDone" />
    <button @click="removeTodo()">R</button>
  </div>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    item: {
      type: Object,
      required: true,
      validator: value => {
        return (
          typeof value['text'] === 'string' &&
          typeof value['isDone'] === 'boolean' &&
          typeof value['id'] === 'number'
        )
      }
    }
  },
  methods: {
    removeTodo() {
      this.$emit('removeTodo', this.item)
    }
  }
}
</script>

<style>
.flex {
  display: flex;
}

.isDoneCheckbox {
  margin-left: 8px;
  margin-top: 2px;
  margin-right: 2px;
}

.text-linethrough {
  text-decoration: line-through;
}
</style>
