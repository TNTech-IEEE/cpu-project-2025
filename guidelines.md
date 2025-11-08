# Contribution Guidelines

This project is run by the Tennessee Tech University IEEE Student Branch. We primarily intend this repository to be used as a learning experience for our students, but we welcome contributions from the wider community as well. To ensure a smooth collaboration process, please follow these guidelines when contributing to the project.

## General Guidelines

1. **Develop on a Separate Branch**  
   Always create a new branch for your work instead of committing directly to the `main` branch. This helps keep the main codebase stable and allows for easier code reviews.

2. **Submit Pull Requests**
    When your work is complete, submit a pull request (PR) to the `main` branch (or an appropriate feature branch). Provide a clear description of the changes you have made and any relevant context. 

3. **Write Clear Commit Messages**
    Use descriptive commit messages that clearly explain the changes you have made. This will help others (and your future self) understand the history of the project.

4. **Remember the Human**
    Be respectful and considerate in your communications. Open source is a collaborative effort, and maintaining a positive environment is crucial. All contributions to this project should adhere to the Tennessee Tech Student Code of Conduct and all other relevant university policies.

## Guidelines for Digital Logic Designs

1. **Use Standard Naming Conventions**  
   Follow consistent naming conventions for files, modules, signals, and variables. This improves readability and maintainability of the code.
    1. Files will follow a format of all lowercase letters with words being separated by underscores, e.g. foo_bar.txt, sample_file.cpp, etc.

2. **Document Your Designs**
    Provide clear documentation for your designs, including block diagrams, truth tables, and timing diagrams where applicable. This will help others understand the functionality and purpose of your designs. Most importantly, provide clear descriptions of what the design does and what all inputs and outputs represent.

3. **Simulate and Test Your Designs**
    Before submitting your designs, ensure that they have been thoroughly simulated and tested. It's far better to catch and fix logic issues early in the design process than later during integration or fabrication.

4. **Use Only Approved Logic Gates and Components**
    Ensure that you only use logic gates and components that are pre-approved for use in this project. This helps maintain compatibility and reliability across the designs while also greatly simplifying the PCB design and fabrication process. Please refer to [this file](./approved_components.md) for a list of approved components. If you wish to use a component that is not currently approved, please open an issue to discuss its inclusion.


## Guidelines for PCB Designs

1. **Match Schematics with Digital Logic Designs**
    Ensure that your PCB schematics accurately reflect the approved digital logic designs. Any discrepancies can lead to functional issues in the final product.

2. **Follow PCB Design Best Practices**
    Adhere to established PCB design best practices, including proper component placement, routing techniques, and power distribution. This will help ensure the reliability and manufacturability of the PCB. Please refer to [this file](./pcb_guidelines.md) for detailed guidelines on PCB design best practices and the conventions we follow in this project.

3. **Design for Manufacturability**
    Keep in mind the manufacturing constraints and capabilities of the PCB fabrication house. Make sure that your DRC (Design Rule Check) settings align with the manufacturer's specifications.

4. **Use Approved Components**
    Only use components that are listed in the approved components document. This ensures compatibility and simplifies the procurement process. As part of this project, will maintain component and footprint libraries of approved components to streamline the design process. 

## Guidelines for Software Development

1. **Follow Coding Standards**
    Adhere to established coding standards and best practices for the programming languages used in this project. This includes proper indentation, naming conventions, and code organization.

2. **Document Your Code**
    Provide clear and concise documentation for your code, including comments, function descriptions, and usage instructions. This will help others understand and maintain the codebase.



