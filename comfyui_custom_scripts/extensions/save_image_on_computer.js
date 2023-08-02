import { app } from "/scripts/app.js";

function addPathWidget(node, inputName, inputData, app) {
	const widget = {
		type: "customtext",
		name,
		get value() {
		    console.log('get save image on computer');
			return 0;
		},
		set value(x) {
			this.inputEl.value = x;
		},
		draw: function (ctx, _, widgetWidth, y, widgetHeight) {},
	};

	widget.parent = node;

	node.addCustomWidget(widget);

	return { minWidth: 400, minHeight: 200, widget };
}


const ext = {
	// Unique name for the extension
	name: "sd-webui-auto-backup",
	async init(app) {
		// Any initial setup to run as soon as the page loads
	},
	async setup(app) {
		// Any setup to run after the app is created
	},
	async addCustomNodeDefs(defs, app) {
		// Add custom node definitions
		// These definitions will be configured and registered automatically
		// defs is a lookup core nodes, add yours into this
	},
	async getCustomWidgets(app) {
		// Return custom widget types
		// See ComfyWidgets for widget examples

		return {
            FILEPATH(node, inputName, inputData, app) {
                return addPathWidget(node, inputName, app);
            },
		}
	},
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		// Run custom logic before a node definition is registered with the graph
		// This fires for every node definition
	},
	async registerCustomNodes(app) {
		// Register any custom node implementations here allowing for more flexibility than a custom node def
	},
	loadedGraphNode(node, app) {
		// Fires for each node when loading/dragging/etc a workflow json or png
		// If you break something in the backend and want to patch workflows in the frontend
		// This is the place to do this
		// This fires for every node on each load
	},
	nodeCreated(node, app) {
		// Fires every time a node is constructed
		// You can modify widgets/add handlers/etc here
	}
};

app.registerExtension(ext);
