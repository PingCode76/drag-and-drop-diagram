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
        <drag v-for="n in numbers" :key="n" class="drag" :data="n" @cut="remove(n)">{{n}}</drag>
      </transition-group>
      <!-- end label transition -->
      <hr class="hr-80">
      <h7> add nodes </h7>
      <hr class="hr-80">
      <h7> add function </h7>
      <hr class="hr-80">
    </div>
    <div class="container">
      <div class="container-diagram">
        <h4> {{ title }} </h4>
        <div class="row">
          <div class="function">

            <!-- new -->
            <div class="group">
              <drop class="copy" @drop="onCopyDrop">
                <span v-for="(n, index) in copied" :key="index">
                  <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="drag" :data="n" @cut="remove(n)">{{n}}</drag>
                  </transition-group>
                </span>
              </drop>
              <drop class="copy" @drop="onCopyDrop1">
                <span v-for="(n, index1) in copied1" :key="index1">
                  <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="drag" :data="n" @cut="remove(n)">{{n}}</drag>
                  </transition-group>
                </span>
              </drop>
              <drop class="copy" @drop="onCopyDrop2">
                <span v-for="(n, index2) in copied2" :key="index2">
                  <transition-group name="list" tag="div">
                    <drag v-for="n in numbers" :key="n" class="drag" :data="n" @cut="remove(n)">{{n}}</drag>
                  </transition-group>
                </span>
              </drop>
            </div>
            
            <!-- end new -->
            <!-- 
            <div class="col">
              <p> Col </p>
              <div class="label">
                <div class="row">
                  <div class="col-lg-3 node-in node"> XX84</div>
                  <div class="col-lg-6 label-center">
                    <p> LabelTxt </p>
                  </div>
                  <div class="col-lg-3 node-out node"> AA34</div>
                </div>
              </div>
            </div>
            <div class="tra">
              <p> Tra </p>
            </div>
            <div class="fer">
              <p> Fer </p>
            </div>
            -->

          </div> <!-- end function-->
        </div> <!-- end row -->
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
            numbers: ["label"],
            numbers1: ["label"],
            numbers2: ["label"],
            copied: [],
            copied1: [],
            copied2: [],
            cut: []
        }
    },
    methods: {
      onCopyDrop(e) {
        this.copied.push(e.data);
      },
      onCopyDrop1(e) {
        this.copied1.push(e.data);
      },
      onCopyDrop2(e) {
        this.copied2.push(e.data);
      },
      remove(n) {
        let index = this.numbers.indexOf(n);
        this.numbers.splice(index, 1);

        let index1 = this.numbers1.indexOf(n);
        this.numbers1.splice(index1, 1);

        let index2 = this.numbers2.indexOf(n);
        this.numbers2.splice(index2, 1);
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
.drag {
  width: 60px;
  height: 60px;
  background-color: rgb(220, 220, 255);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 10px 10px 0 10px;
  font-size: 20px;
  transition: all 0.5s;
}

.group {
  display: flex;
}

.copy {
  margin: 20px 10px;
  border: 1px solid black;
  height: 100px;
  display: inline-block;
  position: relative;
  flex: 1;
}

.cut {
  margin: 20px 10px;
  border: 1px solid black;
  height: 100px;
  display: inline-block;
  position: relative;
  flex: 1;
}

.copy::before {
  content: "COPY";
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