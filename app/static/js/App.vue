<template>
  <draggable :model="model" class="root"></draggable>
</template>

<script>
import { Drag, Drop, DropMask } from "vue-easy-dnd";

//import Draggable from "./js/components/draggable.vue";

export default {
  name: "App",
  components: {
    Draggable
  },

  data: function() {
    return {
      key: 0,
      model: null
    };
  },
  
};
</script>

