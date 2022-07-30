# 5.1 Conditions under which a behavior occurs
Some requirements do not describe continuous behaviors,but behaviors that are performed or provided only under certain conditions; for example, logical or temporary, as is shown below.

1. **Requirements with logical conditions**

    They are used for describing behaviors that are triggered only when a logical condition is met or when an unexpected event occurs 

    *IF **[Condition or event]** THEN (ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD...*

    >If the number of products in a warehouse reach the defined minimum limit then, the inventory subsystem should generate a product replacement alert for that warehouse.
1. **Requirements guided by the state**

    They are used for describing a behavior that must be performed in the system while the system is in a specific state.

    *WHILE|DURING **[Activation state]** (ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD...*

    >While the payment of an invoice from a customer has not been confirmed, the subsystem must send a daily text message to the cell phone number registered by the customer
1. **Requirements with optional elements**

    They are used for describing a behavior that must be performed only if a particular characteristic is included

    *IN CASE **[Included feature]** IS INCLUDED (ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD...*

    This condition is especially useful in domain requirements when you want to incorporate certain requirements depending on the characteristics provided by the product line.

    >In case the text entry action is included, all systems of the test automation framework product line shall provide the tester with the ability to enter a specific text, in a form field.
1. **Requirements with temporary conditions**

    They areused for describing a behavior that must occur after another behavior occurs. They occur sequentially, itmeans, behavior A is done after B.

    *AFTER|BEFORE|AS SOON AS **[Behavior]** (ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD...*

    **AFTER** means that the system must have completed a running behavior before initiating another behavior.

    **BEFORE** means that the system must initiate a behavior before another behavior takes place. AS SOON AS means that the system does not necessarily have to have finished a running behavior before initiating another behavior.

    >After reading the products for a particular location, the Inventory subsystem should providethe warehouse owner with the ability to close the product count for that location.

1. **Requirements with complex conditions**

    For requirements with more complex conditional clauses, it can be necessary to add with keywords as When, While, Where. 

    >When a cash settlement operation is performed on a cash register, while the box is temporarily closed, the point of sale subsystem should show the amount of cash that is in the box.

    Conditional clauses can also be structured using the Boolean operators AND, OR and combined with NOT

    >If a location contains products and the option to delete a location has been selected, then the Inventory Subsystem should display an alert message indicating that the selected location cannot be deleted.

# 5.2 Family of systems, systems or parts of a system

The structure of the second space of the new template is as follows:

*ALL|SOME SYSTEMS OF THE **[Product linename]***

In some cases, we must consider certain behaviors that some systems of the product line must incorporate if certain conditions or restrictions are met, when this happens, we will use the expression:

*THOSE SYSTEMS OF THE **[Product line name]** **[Restriction]***

>In case the action of comparing text is included, those systems of the automation framework product line that only include the option to enter text shall provide the tester with the ability to configure a text for comparison with another element

# 5.3 The degree of priority

To define the priority of the requirements we have used the MoSCoW technique (Clegg and Barker 1994), in which three degrees of priority are established: essential, recommended and
desirable

1. **Essential requirements** 

    These requirements must be implemented to achieve the success of the product or the product line. The word SHALL is used.

1.  **Recommended requirements** 

    These requirements are important, but not necessary to achieve the success of the product or the product line. The word SHOULD is used

1. **Desirable requirements** 

    These requirements are desirable, but not necessary. They could improve the user experience and customer satisfaction. The word COULD is used.

>All systems of the Test Automation product line *shall* incorporate a click action.

>If a motion sensor is activated, then Oktupus system *should* send an instant image to the home owner's email.

# 5.4 The activity

1. Autonomous activity

    No user involved

    *ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD **[Process verb]***
1. User interaction

    A user interacts with the system

    *ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD PROVIDE **[Who?]** WITH THE ABILITY TO **[Process verb]***
1. Interface requirement

    the system performs a behavior dependent on another entity

    *ALL|SOME SYSTEMS OF THE **[Product line name]**)|(THE **[System or part name]**) SHALL|SHOULD|COULD BE ABLE TO **[Process verb]***

    In addition, this structure is completed with the entity with which the system interacts
Mood es un servicio implementado para los amantes de la música que desean subir su estado de animo. Es una plataforma web que por medio de un algortimo de sugerencia usando IA reconozca los estados de animo, y a partir de estos recomiende canciones para estimular sus emociones. A diferencia de otras plataformas reproductoras de música las sugerencias no se daran solo por busquedas sino también por medio de las expresiones faciales con la finalidad de realizar una transición a diferentes estados emocionales.
    - If the behavior is executed by the external system that transmits data to the receiving system interface, then the specification will be complemented by adding:

        FROM **[System or external device name]**

    - If the behavior is performed by the system and interacts or affects another system or external device then the specification will be complemented by adding:

        TOWARDS **[System or external device name]**

    >The point of sale subsystem shall have the ability to read a valid credit card from a branch's dataphone

# 5.5 The object or objects

The ranges in the new template are specified as follows:
1. Single object: *ONE **[Object]***
1. A specific object: *THE **[Object]***
1. Each object of a set: *EACH **[Object]***
1. Multiple objects: ***[X]** **[objects]**, where X is the number of objects*
1. Range of objects: *BETWEEN **[A]** AND **[B]** **[Objects]***, where A is the lower range and B is the upper range
1. All objects in a set: *ALL THE **[Objects]***

>The inventory subsystem should provide the inventory manager with the ability to associate between 1 and 3 bar code reading guns to a cash register.

>As soon as the daily activity cycle ends, the Oktupus system must restart all the sensors connected in the home.

# 5.6 The complementary details

They can be one or several adjectives, as well as a more enriched description of the object, without the risk of altering the proper meaning of the specification of the requirement, and focusing only on describing the details related to the object in question

# 5.7 Conditionality in the object

Sometimes, the behavior of the requirement is conditioned
by the state of an object

*IF AND ONLY IF **[condition]***

It is important to clarify that this condition is optional. It is only given explicitly if the precise object of the requirement requires specifying the condition, therefore, it is not mandatory in the specification of the requirement

>If any sensor exceeds the defined tolerable limits, the Oktupus system should turn on a siren, if and only if the siren is activated.

>The inventory subsystem could provide the warehouse manager with the ability to eliminate a purchase order, if and only if the purchase order has not been dispatched

# 5.8 Verification criterion (adjustment) of the requirement

especially non-functional requirements, it is necessary to establish the degree to which the requirement must be met. It means including “a quantification of the requirement that demonstrates the standard that the product must reach” as part of the specification of each requirement, functional and non-functional.

>If a fault causes the system to stop, the Oktupus system must restart all the sensors in less than 20 seconds.

>The system must provide an ATM with the ability to register a sale in a cash register without presenting more than 2 different screens.

# 5.9 Relax requirements statements for self-adaptive systems

RELAX incorporated several types of operators to address the uncertainty in the properties of the system. Usually, requirements prescribe the behavior using imperatives such as “Must” or “Should”. 

RELAX proposes to establish a simple process to explicitly identify when a requirement should remain unchanged and mandatory and when a requirement can temporarily relax under certain conditions.

1. fuzzy conditions that can be taken by self-adaptive systems to measure different environment variables
1. Awareness Requirements (or AwReqs) to specify requirements about the success or failure of other requirements that can refer to goals, tasks, quality constraints and domain assumptions 
1. constraints that must be
met using certain questions in a conditional manner

---

1. *(AS MANY|AS FEW) AS POSSIBLE*: A requirement must maximize or minimize a certain occurrence of something or a certain amount of objects, as many or as few as possible, thus leading to adaptation.

1. *BEFORE|AFTER|DURING*: A requirement must be met before, during or after a particular event, usually these three operators go after the operators AS MANY AS POSSIBLE, AS FEW AS POSSI- BLE, AS SOON AS POSSIBLE or AS LATE AS POSSIBLE.

1. *(AS EARLY|AS LATE) AS POSSIBLE*: A requirement specifies something that must be fulfilled as early as possible or must be delayed as late as possible.

1. *UNTIL*: A requirement must be maintained until a future position (event).

1. *WITHIN*: A requirement must be maintained for a particular time interval, expressed in units of time.

1. *AT LEAST*: A requirement must meet a minimum frequency or time, until infinity.

1. *EVENTUALLY*: The behavior of the requirement must occur eventually, e.g. it is not completely safe or fixed that the behavior occurs, but the system must be prepared.

1. *AS CLOSE AS POSSIBLE TO*: A requirement
specifies something that happens repeatedly, but the
frequency can be flexible 

>The VMS system must record as many steps as possible during a user's walking activity.

>The VMS system will consume as few units of energy as possible during the normal operation of the intelligent bracelet.

>The VMS system must send an alert to the user who must stop when the physical activity levels (MET 1 ) are as close as possible to 2.

>If a user's vital signs levels are below the userdefined values, then the VMS system must send an alert to the registered emergency phone within 2 seconds.

>The VMS system should check the user's average calories consumed levels eventually.