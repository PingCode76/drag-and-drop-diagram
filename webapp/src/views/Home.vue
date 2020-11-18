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
      <h7> add column </h7>
      <hr class="hr-80">
      <h7> add label </h7>
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
            <div class="col">
              <p> Col </p>
              <div class="label">
                <div class="row">
                  <div class="col-lg-3 node-in node"> XX84</div>
                  <div class="col-lg-6 label-center">
                    <p> LabelTxt </p>
                    <!-- <input v-model="message"> -->
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
          </div> <!-- end function-->
        </div> <!-- end row -->
      </div> <!-- end container diagram-->
    </div> <!-- end container -->
  </div> <!-- end home-->
</template>

<script>
// @ is an alias to /src
import BaseComponent from '../components/BaseComponent.vue'

  export default {
    name: 'Home',
    components: {
      BaseComponent
    },
    data: function(){
        return {
            APImessageGreeting: ''
        }
    },
    created: async function(){
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.APImessageGreeting = gObject.greeting;
    }
  }
</script>
