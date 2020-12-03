<template>
    <div class="group">
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
        <!-- tra -->
        <drop class="copyLabel" @drop="onCopyDropLabel1" :accepts-data="(nTra) => nTra === nTra" accepts-type="boolean">
            <span v-for="(nTra, ColumnTra) in Tra" :key="ColumnTra">
                <transition-group name="list" tag="div">
                    <drag v-for="nTraLabel in labelTra" :key="nTraLabel" class="labels" :data="nTraLabel" @cut="removeTra(ColumnTra)">{{nTraLabel}}
                      <p> {{ ColumnTra }}</p> <!-- tab n label in Tra-->
                      <p> Tra</p>
                      <input class="node-left" v-model="nodeLTra" placeholder="node L">
                      <input class="txt-label" v-model="messageTra" placeholder="txt">
                      <input class="node-right" v-model="nodeRTra" placeholder="node R">
                    </drag>
                </transition-group>
            </span>
        </drop>
        <!-- fer -->
        <drop class="copyLabel" @drop="onCopyDropLabel2" :accepts-data="(nFer) => nFer === nFer" accepts-type="boolean">
            <span v-for="(nFer, ColumnFer) in Fer" :key="ColumnFer">
                <transition-group name="list" tag="div">
                    <drag v-for="nFerLabel in labelFer" :key="nFerLabel" class="labels" :data="nFerLabel" @cut="removeFer(ColumnFer)">{{nFerLabel}}
                      <p> {{ ColumnFer }}</p> <!-- tab n label in Fer-->
                      <p> Fer</p>
                      <input class="node-left" v-model="nodeLFer" placeholder="node L">
                      <input class="txt-label" v-model="messageFer" placeholder="txt">
                      <input class="node-right" v-model="nodeRFer" placeholder="node R">                   
                    </drag> 
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
            labelCol: [""], // label uniq drag !important
            labelTra: [""], // label uniq drag !important
            labelFer: [""], // label uniq drag !important
            Col: [], // label copied in Col
            Tra: [], // label copied in Tra
            Fer: [], // label copied in Fer
            nodeLCol: '', // data Col
            messageCol: '',
            nodeRCol: '',
            nodeLTra : '', // data Tra
            messageTra: '',
            nodeRTra : '',
            nodeLFer : '', // data Tra 
            messageFer : '',
            nodeRFer : '',
            CountCol : 0, // give a number to a label
            CountTra : 0,
            CountFer : 0,
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
      onCopyDropLabel1(e) { 
        this.CountTra = this.CountTra + 1 // Count each label Tra
        this.Tra.push(e.data+"Tra"+this.CountTra);

        console.log(this.Tra); // tab many label : name "label"

      },
      onCopyDropLabel2(e) {
        this.CountFer = this.CountFer + 1 // Count each label Fer
        this.Fer.push(e.data+"Fer"+this.CountFer);

        console.log(this.Fer); // tab many label : name "label"

      },
      removeCol(ColumnCol) {
        console.log(ColumnCol); // get index 
        this.Col.splice(ColumnCol, 1); // delete 1 element in tab with index
        console.log(this.Col);
      },
      removeTra(ColumnTra) {
        console.log(ColumnTra); // get index 
        this.Tra.splice(ColumnTra, 1); // delete 1 element in tab with index
        console.log(this.Tra);
      },
      removeFer(ColumnFer) {
        console.log(ColumnFer); // get index 
        this.Fer.splice(ColumnFer, 1); // delete 1 element in tab with index
        console.log(this.Fer);

        // let indexFer = this.labelFer.indexOf();
        //this.Fer.splice(indexFer, 1);
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