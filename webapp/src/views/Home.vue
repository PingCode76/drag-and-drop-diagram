<template>
  <div class="home">

    <!-- Modal for export data-->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            ...
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <!-- HERE : FORM for save title of record data -->
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>

  <!--
    <br/>
    <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#myModal">
        Save Data
      </button>
  -->

    <BaseComponent/>
    <p> {{ APImessageGreeting }}</p>

    <div class="drag-left">
      <h4> Element </h4>
      <hr class="hr-80">
      <!-- -------------------- Export Drag  --------------------   -->

      <!-- label transition -->
      <h4> add label </h4>
      <transition-group name="list" tag="div">
        <drag v-for="n in label" :key="n" class="label" :data="n" :type="typeof true">{{n}}</drag>
      </transition-group>
      <hr class="hr-80">
      <!-- end label transition -->

      <!-- function transition -->
      <h4> add function </h4>
      <transition-group name="list" tag="div">
        <drag v-for="f in functions" :key="f" class="functions" :data="f" :type="typeof f">{{f}}</drag>
      </transition-group>
      <hr class="hr-80">
      <!-- end function transition -->

<!--
      <button type="button" class="btn btn-danger">
        Import Data
      </button>
-->

      <!-- -------------------- End Export Drag  --------------------   -->
    </div>
    
    <div class="container">
      <div class="container-diagram">

        <!-- component function --> 
        <function></function>

      </div> <!-- end container diagram-->
    </div> <!-- end container -->

    <!-- remove component --> 
    <remove></remove>

  </div> <!-- end home-->
</template>

<script>
// @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";
import BaseComponent from '../components/BaseComponent.vue'
import Function from '../components/Function.vue'
import Remove from '../components/Remove.vue'

  export default {
    name: 'Home',
    components: {
      BaseComponent,
      Drag,
      Function,
      Remove,
    },
    data: function(){
        return {
            APImessageGreeting: '',
            label: ["label"], // label number ( unique drag )
            functions: ["function"], // function ( unique drag ) 
        }
    },
    created: async function(){
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.APImessageGreeting = gObject.greeting;
    },
    methods: {
      onCutDrop(e) {
        this.cut.push(e.data);
      }
    }
  }
</script>

<style>

.home {
    background-color: rgb(6, 143, 129);
    padding-bottom : 50px;
}

/* item drag and drop (drag-left)  */ 
.label {
  width: 170px;
  height: 60px;
  background-color: white;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 10px 10px 0 10px;
  font-size: 20px;
  transition: all 0.5s;
  margin-bottom : 10px ; 
  text-align : center ;
  border-radius: 15px ; 
}

/* item drag and drop */ 
.functions {
  border-radius: 18px ; 
  width: 170px;
  height: 60px;
  background-color: rgb(6, 143, 129);
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

/* structure */
.drag-left {
    background-color: turquoise;
    height: 500px; /* 100% ? */ 
    width: 15%;
    position: fixed;
    left: 0%;
    top: 0%;
    float: left;
    margin-top: 350px;
    padding-top: 50px ; 
    margin-bottom: 200px;
    margin-left: 35px;
    text-align: center;
    border-bottom : 5px burlywood solid ;
    border-top : 5px burlywood solid ;
    border-left : 5px burlywood solid ;
    border-radius: 15px ; 
    vertical-align: center;
}

/* Container ( diagram )  */

.container-diagram {
    border : 5px turquoise solid ;
    border-radius: 15px ; 
    min-height : 700px;
    height: auto;
    margin-top: 50px;
    margin-bottom: 50px;
    text-align: center;
    padding: 15px;
    padding-right: 25px;
    background-color: burlywood;
}
</style>