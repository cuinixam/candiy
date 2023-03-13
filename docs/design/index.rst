Design
######


Event Manager
=============

.. drawio-image:: event_manager.drawio
   :export-scale: 150


The EventManager class is a utility class that can be used in conjunction with the Model-View-Presenter design pattern to facilitate communication between the View and the Presenter. Its primary purpose is to handle events that are raised by the View and forward them to the appropriate Presenter methods.

The class has several methods:

* `create_event_trigger` - Creates a lambda function that can be used to trigger a specific event.

* `subscribe` - Adds a callback function to the list of subscribers for the given `event_id`. If the callback is already subscribed to the event, a ValueError is raised.

* `unsubscribe` - Removes a callback function from the list of subscribers for the given event_id.


By using the EventManager class, the View can raise events using the create_event_trigger method, and the Presenter can subscribe to those events using the subscribe method. When the event is triggered, the EventManager calls all of the registered callbacks for that event, allowing the Presenter to handle the event appropriately. The unsubscribe method can be used to remove callbacks from the list of subscribers if needed.

It's worth noting that the EventManager class, as described above, is actually an implementation of the Observer design pattern. In this pattern, the EventManager acts as the Subject or Observable, while the callbacks registered through the subscribe method serve as the Observers.

When an event is triggered, the EventManager notifies all registered Observers by calling their respective callback functions. This decouples the components of the system and allows for easier maintenance and modifications in the future.

By using the Observer pattern with the EventManager class, the View can raise events without knowing anything about the Presenter, and the Presenter can handle events without knowing anything about the View. This promotes a more modular and flexible architecture, making it easier to develop and maintain complex systems.