<template>
    <div class="group">
        <!-- col -->
        <drop class="copyLabel" @drop="onCopyDropLabel">
            <span v-for="(n, index) in copied" :key="index">
                <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                </transition-group>
            </span>
        </drop>
        <!-- tra -->
        <drop class="copyLabel" @drop="onCopyDropLabel1">
            <span v-for="(n, index1) in copied1" :key="index1">
                <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                </transition-group>
            </span>
        </drop>
        <!-- fer -->
        <drop class="copyLabel" @drop="onCopyDropLabel2">
            <span v-for="(n, index2) in copied2" :key="index2">
                <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="label" :data="n" @cut="remove(n)">{{n}}</drag>
                </transition-group>
            </span>
        </drop>
    </div>
</template>

<script>
  // @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";

  export default {
    name: 'Label',
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
  background-color: rgb(170, 170, 170);
}
</style>