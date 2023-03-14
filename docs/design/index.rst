Design
######

.. drawio-image:: figures/design_pattern.drawio
   :export-scale: 150

In this diagram, you can see the three main components: View, Presenter, and Event Manager.
The Event Manager handles the events and subscriptions, while the Presenter mediates between the View and the underlying functionality.
The View interacts with the user and triggers events that are handled by the Event Manager.
The Presenter subscribes to the Event Manager to handle these events and updates the View accordingly.

.. drawio-image:: figures/main_classes.drawio
   :export-scale: 150

The implementation above uses the Model-View-Presenter (MVP) design pattern along with the Event Manager to handle events and communication between the components.
Here are some advantages of this implementation:

* **Separation of Concerns:**
   This pattern pattern separates the responsibilities of the View and Presenter into distinct components, which makes the code easier to read, test, and maintain.
   The Event Manager also helps to decouple the components, making it easier to modify and extend the code without affecting other parts.
* **Testability:**
   The Presenter acts as a mediator between the View and the underlying functionality, which allows for easy unit testing of the Presenter without needing to test the user interface.
* **Flexibility:**
   It allows for different user interfaces to be used with the same underlying functionality.
   For example, if we wanted to switch from a graphical user interface to a command-line interface, we could do so without affecting the underlying functionality of the application.


Event Manager
=============

The EventManager class is a utility class that can be used in conjunction with the Model-View-Presenter design pattern to facilitate communication between the View and the Presenter.
Its primary purpose is to handle events that are raised by the View and forward them to the appropriate Presenter methods.


By using the EventManager class, the View can raise events using the create_event_trigger method, and the Presenter can subscribe to those events using the subscribe method.
When the event is triggered, the EventManager calls all of the registered callbacks for that event, allowing the Presenter to handle the event appropriately.
The unsubscribe method can be used to remove callbacks from the list of subscribers if needed.

It's worth noting that the EventManager class, as described above, is actually an implementation of the Observer design pattern.
In this pattern, the EventManager acts as the Subject or Observable, while the callbacks registered through the subscribe method serve as the Observers.

When an event is triggered, the EventManager notifies all registered Observers by calling their respective callback functions. This decouples the components of the system and allows for easier maintenance and modifications in the future.

By using the Observer pattern with the EventManager class, the View can raise events without knowing anything about the Presenter, and the Presenter can handle events without knowing anything about the View. This promotes a more modular and flexible architecture, making it easier to develop and maintain complex systems.

.. autoclass:: candiy.presenter.event_manager::EventManager
   :members:
   :undoc-members:
