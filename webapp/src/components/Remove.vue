<template>

  <!-- desk -->
  <div class="trash">
    <drop class="cut" @drop="onCutDrop" mode="cut">
      <!-- 
      <span v-if="(nCol, index) in cut" :key="index"> </span>
      <span v-if="(nTra, index1) in cut" :key="index1"> </span>
      <span v-if="(nFer, index2) in cut" :key="index2"> </span>
      -->
      
      <!-- <span v-if="(n, index) in cut" :key="index"> </span> -->
      <i class="far fa-trash-alt"></i>
    </drop>
  </div>

  <!-- end desk -->
</template>

<script>
  // @ is an alias to /src
import { Drag, Drop, DropMask } from "vue-easy-dnd";

  export default {
    name: 'Remove',
    components: {
      Drop,
    },
    data: function(){
        return {
            APImessageGreeting: '',
            cut: [],
        }
    },
    created: async function(){
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.APImessageGreeting = gObject.greeting;
    },
    /* method ? */
    methods: {
        onCutDrop(e) {
            this.cut.push(e.data);
        }
    }
  }
</script>

<style>
/* desk */ 
.trash {
  background-color: rgb(6, 143, 129);
  width : 350px ; 
  margin-right : 150px ; 
  height : 150px ; 
  position: fixed;
  right: 0%;
  top: 0%;
  margin-top: 350px;
  margin-bottom: 200px;
  margin-left: 100px;
  margin-right: 100px;
  text-align: center;
  border-bottom : 5px burlywood solid ;
  border-top : 5px burlywood solid ;
  border-right : 5px burlywood solid ;
  border-radius: 15px ; 
  vertical-align: center;
}

.fa-trash-alt {
    font-size : 70px ; 
    margin-top: 10px ; 
    color: rgb(6, 143, 129) ;
}
.cut {
  background-color : white ;
  margin: 20px 10px;
  border: 3px solid burlywood;
  border-radius: 15px ; 
  height: 100px;
  width : 250px ;
  display: inline-block;
  position: relative;
  flex: 1;
}

.cut::before {
  /* content: "CUT"; */
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  color: rgba(0, 0, 0, 0.4);
  font-size: 25px;
  font-weight: bold;
}
</style>