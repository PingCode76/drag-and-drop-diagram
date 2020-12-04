<template>
    <!-- col -->
    <drop class="copyLabel" @drop="onCopyDropLabel" :accepts-data="(nCol) => nCol === nCol" accepts-type="boolean">
        <span v-for="(nCol, ColumnCol) in Col" :key="ColumnCol">
            <transition-group name="list" tag="div">
                <drag v-for="nColLabel in labelCol" :key="nColLabel" class="labels" :data="ColumnCol" @cut="removeCol(ColumnCol)">{{nColLabel}}                                   
                    <!-- <p> {{ Col }}</p> --> <!-- tab col "label"-->
                    <p> {{ ColumnCol }}</p> <!-- tab n label in col-->
                    <p> Col</p>
                    <input class="node-left" v-model="nodeLCol" placeholder="node L"> <!-- <p> Data form is : {{ nodeL }} </p> --> 
                    <input class="txt-label" v-model="messageCol" placeholder="txt">
                    <input class="node-right" v-model="nodeRCol" placeholder="node R">
                </drag>
            </transition-group>
        </span>
    </drop>
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
            labelCol: [""], // label uniq drag !important
            Col: [], // label copied in Col
            nodeLCol: '', // data Col
            messageCol: '',
            nodeRCol: '',
            CountCol : 0, // give a number to a label
        }
    },
    methods: {
      onCopyDropLabel(e) {
        this.CountCol = this.CountCol + 1 // Count each label Col
        this.Col.push(e.data+"Col"+this.CountCol);

        console.log(this.Col); // tab many label : name "label1.."

        // API info send /AddLabel/title/node1/node2/FunctionNumber/Column for register one label
        console.log(this.Col[this.Col.length -1 ]); // title element drop // count 
        // node 1
        // node 2  
        console.log("function number")// fonction number 
        console.log("Col");// column ( col , Tra , Fer)
      },
      removeCol(ColumnCol) {
        console.log(ColumnCol); // get index 
        this.Col.splice(ColumnCol, 1); // delete 1 element in tab with index
        console.log(this.Col);
      }
    },
    created: async function(){
        // send label with API : /label/title/NodeR/NodeL/Functionnumber/Column
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.APImessageGreeting = gObject.greeting;
    }
  }
</script>

<style>

/* item in diagram */
.labels {
  width: 270px;
  height: 140px;
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
.node-left {
  width : 75px ; 
  height:50%;
  border-radius: 35px;
  text-align: center ;
  background-color : turquoise ; 
  color : black ;
}

.node-right {
  width : 75px ; 
  height:50%;
  border-radius: 35px;
  text-align: center ;
  background-color : turquoise ; 
  color : black ;
}

.txt-label {
  width: 130px ; 
  margin : 15px;
}
.copyLabel::before {
  /* content: "add label"; */
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
  border-radius: 15px ; 
}
</style>