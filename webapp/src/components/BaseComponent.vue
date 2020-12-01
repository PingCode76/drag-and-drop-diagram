// ./components/BaseComponent.vue
<script>
  export default {
	name: 'BaseComponent',
  props: ['title'],
  }
</script>

<template>
  <div id="nav">
    <router-link to="/">
      Home
    </router-link> |
    <router-link to="/about">
      About
    </router-link>
    <br/><br/><br/><br/>
  </div>
</template>

<style>
	a {
		text-decoration: none;
	}
</style>