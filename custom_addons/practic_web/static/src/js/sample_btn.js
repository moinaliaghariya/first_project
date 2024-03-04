odoo.define("wb_pos.WebButton", function(require){
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sal.Registries");

    class SampleButton extend PosComponent{

    }
    SampleButton.template = "SampleButton";
    ProductScreen.addControlButton({
        component: SampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],
    });

    Registries.Component.add(SampleButton);
    return SampleButton;

})
