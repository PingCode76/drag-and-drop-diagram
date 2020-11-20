<template>
    <!-- function drag label in function -->
    <drop class="copyFunction" @drop="onCopyDropFunctions">

        <span v-for="(f, function1) in copiedFunction" :key="function1">
        
        <transition-group name="list" tag="div">
            <!-- drag insert -->
            <drag v-for="f in functions" :key="f" class="function" :data="f" @cut="remove(f)">{{f}}
            
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
                        </div>
                    </div> <!-- end function-->
                </div> <!-- end row -->

            </drag>  
            <!-- drag insert end -->

        </transition-group>
        </span>
    </drop>
    <!-- end function drag label in function -->
</template>

<script>
  // @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";

  export default {
    name: 'Function',
    components: {
      Drag,
      Drop,
    },
    data: function(){
        return {
            APImessageGreeting: '',
            numbers: ["label"], // label uniq drag !important
            functions: ["function"], // function uniq drag !important
            copied: [], // label copied number 
            copied1: [],
            copied2: [],
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
    width: 95%;
    min-height: 150px;
    height: auto;
    margin : auto;
    margin-top: 10px;
    margin-bottom: 45px ; 
    background-color : blue; 
}

</style>