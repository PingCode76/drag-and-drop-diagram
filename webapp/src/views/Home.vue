<template>
  <div class="home">
    <BaseComponent title="Application Template"/>
    <p> {{ title }} </p>
    <p> {{ APImessageGreeting }}</p>

    <div class="drag-left">

      <button type="button" class="btn btn-danger">
        Export Data
      </button>

      <h4> Element </h4>
      <hr class="hr-80">
      <!-- -------------------- Export Drag  --------------------   -->

      <!-- label transition -->
      <h7> add label </h7>
      <transition-group name="list" tag="div">
        <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
      </transition-group>
      <hr class="hr-80">
      <!-- end label transition -->

      <!-- label transition -->
      <h7> add function </h7>
      <transition-group name="list" tag="div">
        <drag v-for="f in functions" :key="f" class="functions" :data="f" @cut="remove(f)">{{f}}</drag>
      </transition-group>
      <hr class="hr-80">
      <!-- end label transition -->

      <!-- node transition -->
      <h7> add nodes </h7>
      <hr class="hr-80">
      <!-- end node transition -->

      <!-- -------------------- End Export Drag  --------------------   -->
      
    </div>
    <div class="container">
      <div class="container-diagram">
        <h4> {{ title }} </h4>

        <!-- component function --> 
        <function></function>

      </div> <!-- end container diagram-->
    </div> <!-- end container -->
  </div> <!-- end home-->
</template>

<script>
// @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";
import BaseComponent from '../components/BaseComponent.vue'
import Function from '../components/Function.vue'

  export default {
    name: 'Home',
    components: {
      BaseComponent,
      Drag,
      Function,
    },
    data: function(){
        return {
            APImessageGreeting: '',
            numbers: ["label"], // label number ( unique drag )
            functions: ["function"], // function ( unique drag ) 
        }
    },
    created: async function(){
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.APImessageGreeting = gObject.greeting;
    }
  }
</script>

<style>

/* item drag and drop */ 
.label {
  width: 170px;
  height: 60px;
  background-color: green;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 10px 10px 0 10px;
  font-size: 20px;
  transition: all 0.5s;
  margin-bottom : 10px ; 
}

/* item drag and drop */ 
.functions {
  width: 170px;
  height: 60px;
  background-color: blue;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 10px 10px 0 10px;
  font-size: 20px;
  transition: all 0.5s;
  margin-bottom : 10px ; 
}

/* other */ 
.drop-allowed {
  background-color: rgba(0, 255, 0, 0.2);
}

.drop-forbidden {
  background-color: rgba(255, 0, 0, 0.2);
}

.drop-in {
  box-shadow: 0 0 5px rgba(0, 0, 255, 0.4);
}

.list-enter,
.list-leave-to {
  opacity: 0;
}

.list-leave-active {
  position: absolute;
}
</style>