// ./components/BaseComponent.vue
<script>
  export default {
	name: 'BaseComponent',
  props: ['title'],
  }
</script>

<template>
  <div class="navbar-home">
    <div id="nav">
      <router-link to="/">
        Home
      </router-link> |
      <router-link to="/about">
        About
      </router-link>
      <br/><br/><br/><br/>
    </div>
  </div>
</template>

<style>
	a {
		text-decoration: none;
  }
  /*
  .navbar-home{
  border: 1px solid grey;
  border-radius: 5px;
  }
  */
  
</style>