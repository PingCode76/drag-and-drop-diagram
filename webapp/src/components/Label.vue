<template>
    <div class="group">
        <!-- col -->
        <drop class="copyLabel" @drop="onCopyDropLabel" :accepts-data="(nCol) => nCol === nCol" accepts-type="boolean">
            <span v-for="(nCol, ColumnCol) in Col" :key="ColumnCol">
                <transition-group name="list" tag="div">
                    <drag v-for="nColLabel in labelCol" :key="nColLabel" class="labels" :data="nColLabel" @cut="removeCol(nColLabel)">{{nColLabel}}
                      <p> Col</p>
                      <input class="node-left" v-model="nodeL" placeholder="node L"> <!-- <p> Data form is : {{ nodeL }} </p> --> 
                      <input class="txt-label" v-model="message" placeholder="txt">
                      <input class="node-right" v-model="nodeR" placeholder="node R">
                    </drag>
                </transition-group>
            </span>
        </drop>
        <!-- tra -->
        <drop class="copyLabel" @drop="onCopyDropLabel1" :accepts-data="(nTra) => nTra === nTra" accepts-type="boolean">
            <span v-for="(nTra, ColumnTra) in Tra" :key="ColumnTra">
                <transition-group name="list" tag="div">
                    <drag v-for="nTraLabel in labelTra" :key="nTraLabel" class="labels" :data="nTraLabel" @cut="removeTra(nTraLabel)">{{nTraLabel}}
                      <p> Tra</p>
                      <input class="node-left" v-model="nodeL" placeholder="node L">
                      <input class="txt-label" v-model="message" placeholder="txt">
                      <input class="node-right" v-model="nodeR" placeholder="node R">
                    </drag>
                </transition-group>
            </span>
        </drop>
        <!-- fer -->
        <drop class="copyLabel" @drop="onCopyDropLabel2" :accepts-data="(nFer) => nFer === nFer" accepts-type="boolean">
            <span v-for="(nFer, ColumnFer) in Fer" :key="ColumnFer">
                <transition-group name="list" tag="div">
                    <drag v-for="nFerLabel in labelFer" :key="nFerLabel" class="labels" :data="nFerLabel" @cut="removeFer(nFerLabel)">{{nFerLabel}}
                      <p> Fer</p>
                      <input class="node-left" v-model="nodeL" placeholder="node L">
                      <input class="txt-label" v-model="message" placeholder="txt">
                      <input class="node-right" v-model="nodeR" placeholder="node R">                   
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
            Col: [], // label copied in colum 
            Tra: [],
            Fer: [],
        }
    },
    methods: {
      onCopyDropLabel(e) {
        this.Col.push(e.data);
      },
      onCopyDropLabel1(e) {
        this.Tra.push(e.data);
      },
      onCopyDropLabel2(e) {
        this.Fer.push(e.data);
      },
      removeCol(nColLabel) {
        let indexCol = this.labelCol.indexOf(nColLabel);
        this.Col.splice(indexCol, 1);
      },
      removeTra(nTraLabel) {
        let indexTra = this.labelTra.indexOf(nTraLabel);
        this.Tra.splice(indexTra, 1);
      },
      removeFer(nFerLabel) {
        let indexFer = this.labelFer.indexOf(nFerLabel);
        this.Fer.splice(indexFer, 1);
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