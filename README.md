# Genomics Data Visualization Web App

An interactive web application for visualizing genomics data including genome sequences, gene annotations, orthogroups, and functional annotations. Built as a static web app that can be hosted on GitHub Pages.

## Important

`folder_to_json.py` must be placed inside the `excel_output` folder and ran, it will then automatically load all excel files from that folder upon clicking analysis to be loaded in main page.

## Features

### 🧬 Genome Browser
- Upload and visualize FASTA genome files (.fa, .fasta)
- Upload and display GFF gene annotation files (.gff, .gff3)
- Interactive gene search and navigation
- Customizable flanking region visualization (upstream/downstream)
- Gene model rendering with exons, CDS, and nested gene support
- Zoom and pan functionality for detailed exploration

### 📊 Orthogroups Viewer
- Upload CSV files containing orthogroup data
- Filter by keywords and cluster IDs
- Interactive table with sortable columns
- Detailed modal views for each orthogroup
- Integration with genome browser for gene visualization

### 📋 Annotations Viewer
- Upload Excel files (.xlsx) with gene annotations
- Advanced search and filtering capabilities
- Export filtered results to CSV
- Detailed annotation views with functional information
- Cross-reference with genome browser

### 🎨 Modern UI
- Responsive design that works on desktop and mobile
- Tabbed interface for easy navigation
- Drag-and-drop file upload
- Interactive modals and notifications
- Clean, modern styling with smooth animations

## Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No server setup required - this is a static web application

### Installation
1. Clone or download this repository
2. Open `index.html` in a web browser
3. Start uploading your genomics data files

### Usage

#### Genome Browser
1. Click on the "Genome Browser" tab
2. Upload a FASTA file containing your genome sequence
3. Upload a GFF file containing gene annotations
4. Use the search box to find specific genes
5. Adjust flanking regions to see more context around genes
6. Click on gene models to see detailed information

#### Orthogroups
1. Click on the "Orthogroups" tab
2. Upload a CSV file containing orthogroup data
3. Use the keyword search to filter orthogroups
4. Filter by cluster ID ranges
5. Click on rows to see detailed information
6. Use "View in Genome Browser" to see genes in genomic context

#### Annotations
1. Click on the "Annotations" tab
2. Upload an Excel file (.xlsx) containing gene annotations
3. Use the search box to find specific annotations
4. Apply filters to narrow down results
5. Click on rows for detailed views
6. Export filtered results to CSV

## File Formats

### Supported File Types
- **FASTA**: `.fa`, `.fasta` - Genome sequences
- **GFF**: `.gff`, `.gff3` - Gene annotations
- **CSV**: `.csv` - Orthogroup data
- **Excel**: `.xlsx` - Annotation data

### Expected Data Structure

#### GFF Files
Standard GFF3 format with the following features:
- Gene features with ID attributes
- Exon and CDS features linked to parent genes
- Proper coordinate systems (1-based)

#### CSV Files (Orthogroups)
Expected columns:
- Cluster ID
- Gene IDs
- Functional annotations
- Species information

#### Excel Files (Annotations)
Expected columns:
- Gene ID
- Functional description
- GO terms
- Pathway information
- Additional metadata

## Development

### Technologies Used
- **HTML5**: Semantic markup and modern web standards
- **CSS3**: Responsive design with flexbox and grid
- **JavaScript ES6+**: Modern JavaScript features
- **D3.js**: Data visualization and SVG manipulation
- **xlsx.js**: Excel file parsing

### Project Structure
```
webpage/
├── index.html              # Main application file
├── styles/
│   └── main.css           # All styling
├── js/
│   ├── utils.js           # Utility functions
│   ├── genomeViewer.js    # Genome browser logic
│   ├── orthogroupsViewer.js # Orthogroups functionality
│   └── annotationsViewer.js # Annotations handling
└── README.md              # This file
```
## Acknowledgments
- D3.js community for excellent visualization tools
- Modern web standards that make client-side genomics possible
- Open source genomics file format specifications
