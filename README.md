# Genomics Data Visualization Web App

An interactive web application for visualizing genomics data including genome sequences, gene annotations, orthogroups, and functional annotations. Built as a static web app that can be hosted on GitHub Pages.

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

### Key Features of the Code
- **Modular Design**: Each major feature is in its own JavaScript file
- **Error Handling**: Comprehensive error handling with user feedback
- **Performance**: Efficient DOM manipulation and data processing
- **Accessibility**: Semantic HTML and keyboard navigation support
- **Responsive**: Works on all screen sizes

## Deployment

### GitHub Pages
1. Push your code to a GitHub repository
2. Go to repository Settings > Pages
3. Select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Your app will be available at `https://username.github.io/repository-name`

### Other Static Hosting
This app can be hosted on any static hosting service:
- Netlify
- Vercel
- GitHub Pages
- Firebase Hosting
- Amazon S3 + CloudFront

## Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License
This project is open source and available under the MIT License.

## Support
For issues and feature requests, please create an issue in the GitHub repository.

## Acknowledgments
- D3.js community for excellent visualization tools
- Modern web standards that make client-side genomics possible
- Open source genomics file format specifications
