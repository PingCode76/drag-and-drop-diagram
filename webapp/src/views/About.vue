<template>
  <div class="about">
    <BaseComponent title="Application Template"/>
    <h1>This is an about page</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import BaseComponent from '../components/BaseComponent.vue'

  export default {
    name: 'About',
    components: {
      BaseComponent
    }
  }
</script>