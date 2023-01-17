import { reactive } from 'vue';

export const store = reactive({

        source: "http://localhost/api.php",
        countries: [],
        jsonFolder: "http://localhost/pathJson.php",
        jsonList: [],
        selectedJson: "" + ".json",
        pickedSave: false,
        


}); 


