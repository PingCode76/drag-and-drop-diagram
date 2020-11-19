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
      <h7> add label </h7>

      <!-- label transition -->
      <transition-group name="list" tag="div">
        <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
      </transition-group>
      <!-- end label transition -->

      <hr class="hr-80">
      <h7> add nodes </h7>
      <hr class="hr-80">
      <h7> add function </h7>

      <!-- label transition -->
      <transition-group name="list" tag="div">
        <drag v-for="f in functions" :key="f" class="functions" :data="f" @cut="remove(f)">{{f}}</drag>
      </transition-group>
      <!-- end label transition -->

      <hr class="hr-80">
    </div>
    <div class="container">
      <div class="container-diagram">
        <h4> {{ title }} </h4>

        <!-- base function/label -->
        <div class="row">
          <div class="function">
            <div class="group">
              <drop class="copyLabel" @drop="onCopyDropLabel">
                <span v-for="(n, index) in copied" :key="index">
                  <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                  </transition-group>
                </span>
              </drop>
              <drop class="copyLabel" @drop="onCopyDropLabel1">
                <span v-for="(n, index1) in copied1" :key="index1">
                  <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                  </transition-group>
                </span>
              </drop>
              <drop class="copyLabel" @drop="onCopyDropLabel2">
                <span v-for="(n, index2) in copied2" :key="index2">
                  <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                  </transition-group>
                </span>
              </drop>
            </div> <!-- end group -->
          </div> <!-- end function-->
        </div> <!-- end row -->
        <!-- end base function/label -->

        <!-- function drag label in function -->
        <drop class="copyFunction" @drop="onCopyDropFunctions">
          <span v-for="(f, function1) in copiedFunction" :key="function1">
            <transition-group name="list" tag="div">
              <!-- drag insert -->
              <drag v-for="f in functions" :key="f" class="function" :data="f" @cut="remove(f)">{{f}}
              
                <div class="row">
                  <div class="function">
                    <!-- new -->
                    <div class="group">
                      <drop class="copyLabel" @drop="onCopyDropLabel">
                        <span v-for="(n, index) in copied" :key="index">
                          <transition-group name="list" tag="div">
                            <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                          </transition-group>
                        </span>
                      </drop>
                      <drop class="copyLabel" @drop="onCopyDropLabel1">
                        <span v-for="(n, index1) in copied1" :key="index1">
                          <transition-group name="list" tag="div">
                            <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                          </transition-group>
                        </span>
                      </drop>
                      <drop class="copyLabel" @drop="onCopyDropLabel2">
                        <span v-for="(n, index2) in copied2" :key="index2">
                          <transition-group name="list" tag="div">
                            <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                          </transition-group>
                        </span>
                      </drop>
                    </div>
                  </div> <!-- end function-->
                </div> <!-- end row -->

              </drag>  
              <!-- drag insert end -->

            </transition-group>
          </span>
        </drop>
        <!-- end function drag label in function -->
        
      </div> <!-- end container diagram-->
    </div> <!-- end container -->
  </div> <!-- end home-->
</template>

<script>
// @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";
import BaseComponent from '../components/BaseComponent.vue'

  export default {
    name: 'Home',
    components: {
      BaseComponent,
      Drag,
      Drop,
    },
    data: function(){
        return {
            APImessageGreeting: '',
            numbers: ["label"], // label numer 
            numbers1: ["label"],
            numbers2: ["label"],
            copied: [], // label copied number 
            copied1: [],
            copied2: [],
            cut: [],
            functions: ["function"], // function
            copiedFunction: [], // function 
        }
    },
    methods: {
      onCopyDropLabel(e) {
        this.copied.push(e.data);
      },
      onCopyDropLabel1(e) {
        this.copied1.push(e.data);
      },
      onCopyDropLabel2(e) {
        this.copied2.push(e.data);
      },
      onCopyDropFunctions(e) {
        this.copiedFunction.push(e.data);
      },
      remove(n) {
        let index = this.numbers.indexOf(n);
        this.numbers.splice(index, 1);

        let index1 = this.numbers1.indexOf(n);
        this.numbers1.splice(index1, 1);

        let index2 = this.numbers2.indexOf(n);
        this.numbers2.splice(index2, 1);

        let function1 = this.functions.indexOf(f);
        this.functions.splice(function1, 1)
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

.group {
  display: flex;
}

.copyLabel {
  margin: 20px 10px;
  border: 1px solid black;
  min-height: 100px;
  height: auto;
  display: inline-block;
  position: relative;
  flex: 1;
}
/* function */
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
  background-color: rgba(25,25,25,0.2);
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

.cut {
  margin: 20px 10px;
  border: 1px solid black;
  height: 100px;
  display: inline-block;
  position: relative;
  flex: 1;
}

.copyLabel::before {
  content: "add label"; 
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  color: rgba(0, 0, 0, 0.4);
  font-size: 25px;
  font-weight: bold;
}

.cut::before {
  content: "CUT";
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  color: rgba(0, 0, 0, 0.4);
  font-size: 25px;
  font-weight: bold;
}

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