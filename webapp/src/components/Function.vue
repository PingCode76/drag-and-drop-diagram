<template>
  <!-- function drag label in function -->
  <drop class="copyFunction" @drop="onCopyDropFunctions" :accepts-data="(f) => f === f" accepts-type="string">
    <span v-for="(f, function1) in copiedFunction" :key="function1">
      <transition-group name="list" tag="div">
        <drag v-for="f in functions" :key="f" class="function" :data="f" @cut="remove(f)">{{f}}
          <div class="row">
            <div class="function">
              <!-- label Component -->
              <Label></Label>
            </div> <!-- end function-->
          </div> <!-- end row -->
        </drag>  
      </transition-group>
    </span>
  </drop>
  <!-- end function drag label in function -->
</template>

<script>
  // @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";
import Label from '../components/Label.vue'

  export default {
    name: 'Function',
    components: {
      Drag,
      Drop,
      Label,
    },
    data: function(){
        return {
            APImessageGreeting: '',
            functions: ["function"], // function uniq drag !important
            copiedFunction: [], // function result drop
            CountFunction : 0,
        }
    },
    methods: {
      onCopyDropFunctions(e) {
        this.CountFunction = this.CountFunction + 1 // Count each function
        this.copiedFunction.push(e.data+this.CountFunction);

        console.log(this.copiedFunction);
      },
      remove(f) {
        let function1 = this.functions.indexOf(f);
        this.functions.splice(function1, 1);
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

.copyFunction {
  width: 100%;
  margin: 20px 10px;
  border: 1px solid black;
  min-height: 100px;
  height: auto;
  display: inline-block;
  position: relative;
  flex: 1;
  border : 3px grey solid ;
  border-radius: 18px ; 
  /* background-color: rgba(25,25,25,0.2); */
}

.copyFunction::before {
  content: "add function"; 
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  color: rgba(0, 0, 0, 0.4);
  font-size: 25px;
  font-weight: bold;
}

/* div function */ 
.function {
    border-radius: 18px ; 
    width: 95%;
    min-height: 150px;
    height: auto;
    margin : auto;
    margin-top: 10px;
    margin-bottom: 45px ; 
    background-color: rgb(6, 143, 129); 
}

</style>