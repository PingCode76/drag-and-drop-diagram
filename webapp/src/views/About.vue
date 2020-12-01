<template>
  <div class="about">
    <BaseComponent/>
    <h5> Drag and Drop Diagram </h5>

    <ul>
      <li> step 1  : Drag function in blue space</li>
      <li> Step 2  : Drag Label in green space</li>
      <li> step 3  : Drag node in green space ( in label )</li>
      <li> export Data with button</li>
    </ul>
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