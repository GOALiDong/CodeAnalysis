I need help analyzing and fixing issues in my project. Here's the code structure and contents:

1. Project Overview:
# InstAnalyst-AI: Requirements Analysis System

## Overview
InstAnalyst-AI is a comprehensive requirements analysis system that helps organizations streamline their requirements gathering and management process. The system leverages AI to analyze transcripts, identify requirements, detect gaps, and manage stakeholder interactions.

## Features
- 🎯 Automated requirements extraction from transcripts
- 👥 Stakeholder management and analysis
- 📊 Gap analysis and tracking
- 🔄 Real-time requirements updates
- 📝 Transcript management and processing
- 📈 Analytics and reporting
- 🔐 Secure authentication and authorization

## Technology Stack

### Frontend
- Vue.js 3
- Vuetify 3
- Pinia (State Management)
- Vue Router
- Axios

### Backend
- Node.js
- Express.js
- SQL Server 2019
- Windows Authentication
- OpenAI API Integration

## Project Structure

```
InstAnalyst-AI/
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   ├── store/
│   │   ├── services/
│   │   └── utils/
│   ├── public/
│   ├── .env
│   └── package.json
│
└── backend/
    ├── src/
    │   ├── config/
    │   ├── controllers/
    │   ├── middleware/
    │   ├── models/
    │   ├── routes/
    │   └── services/
    ├── database/
    │   └── schema.sql
    ├── .env
    └── package.json
```

## Prerequisites
- Node.js (v14 or higher)
- SQL Server 2019
- Windows Authentication enabled
- SQL Server Management Studio (SSMS)
- Visual Studio Code (recommended)

## Installation

### Backend Setup
1. Clone the repository
```bash
git clone https://github.com/your-username/InstAnalyst-AI.git
cd InstAnalyst-AI/backend
```

2. Install dependencies
```bash
npm install
```

3. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` with your SQL Server details and other configurations.

4. Run database schema
- Open SQL Server Management Studio
- Connect using Windows Authentication
- Execute the script in `database/schema.sql`

5. Start the backend server
```bash
npm run dev
```

### Frontend Setup
1. Navigate to frontend directory
```bash
cd ../frontend
```

2. Install dependencies
```bash
npm install
```

3. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` with your API endpoint and other configurations.

4. Start the frontend development server
```bash
npm run dev
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Transcripts
- `GET /api/transcripts` - Get all transcripts
- `POST /api/transcripts` - Upload new transcript
- `GET /api/transcripts/:id` - Get transcript details
- `PUT /api/transcripts/:id` - Update transcript
- `DELETE /api/transcripts/:id` - Delete transcript

### Requirements
- `GET /api/requirements` - Get all requirements
- `POST /api/requirements` - Create new requirement
- `GET /api/requirements/:id` - Get requirement details
- `PUT /api/requirements/:id` - Update requirement
- `DELETE /api/requirements/:id` - Delete requirement

### Gaps
- `GET /api/gaps` - Get all gaps
- `POST /api/gaps` - Create new gap
- `GET /api/gaps/:id` - Get gap details
- `PUT /api/gaps/:id` - Update gap
- `DELETE /api/gaps/:id` - Delete gap

### Stakeholders
- `GET /api/stakeholders` - Get all stakeholders
- `POST /api/stakeholders` - Add new stakeholder
- `GET /api/stakeholders/:id` - Get stakeholder details
- `PUT /api/stakeholders/:id` - Update stakeholder
- `DELETE /api/stakeholders/:id` - Delete stakeholder

## Database Schema

### Users
```sql
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Email NVARCHAR(255) UNIQUE NOT NULL,
    FirstName NVARCHAR(100),
    LastName NVARCHAR(100),
    Role NVARCHAR(50),
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE()
)
```

### Transcripts
```sql
CREATE TABLE Transcripts (
    TranscriptID INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(255) NOT NULL,
    Content NTEXT,
    Status NVARCHAR(50),
    CreatedBy INT FOREIGN KEY REFERENCES Users(UserID),
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE()
)
```

### Requirements
```sql
CREATE TABLE Requirements (
    RequirementID INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(255) NOT NULL,
    Description NTEXT,
    Type NVARCHAR(50),
    Priority NVARCHAR(50),
    Status NVARCHAR(50),
    TranscriptID INT FOREIGN KEY REFERENCES Transcripts(TranscriptID),
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE()
)
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Guidelines

### Code Style
- Use ESLint and Prettier for code formatting
- Follow Vue.js Style Guide for frontend code
- Use meaningful variable and function names
- Write comments for complex logic

### Git Commit Messages
- Use clear and descriptive commit messages
- Follow conventional commits format
- Reference issue numbers when applicable

### Testing
- Write unit tests for critical functions
- Test API endpoints with Postman/Insomnia
- Perform integration testing before deployment

## Deployment

### Backend Deployment
1. Set up production environment variables
2. Build the application
```bash
npm run build
```
3. Start the server
```bash
npm start
```

### Frontend Deployment
1. Update API endpoint in production environment
2. Build the application
```bash
npm run build
```
3. Deploy the `dist` folder to your web server

## Troubleshooting

### Common Issues
1. Database Connection Issues
   - Verify SQL Server is running
   - Check Windows Authentication credentials
   - Ensure correct server name in configuration

2. API Connection Issues
   - Check API endpoint configuration
   - Verify CORS settings
   - Check network connectivity

3. Build Issues
   - Clear npm cache
   - Delete node_modules and reinstall
   - Update Node.js version

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For support, email support@instanalyst.com or open an issue in the repository.

## Authors
- Your Name - *Initial work* - [YourGithub](https://github.com/yourusername)

## Acknowledgments
- OpenAI for GPT integration
- Vue.js team for the amazing framework
- All contributors who have helped shape this project

---
**Note**: Replace placeholder values (URLs, emails, usernames) with actual project-specific information before using this README.

This README provides a comprehensive guide for setting up, developing, and deploying the InstAnalyst-AI system. It includes all necessary information for both frontend and backend development, as well as deployment and troubleshooting guidance.

2. I'm specifically looking for:
- Bug fixes
- remove the login feature. anyone with the link access can use this app.
- Security issues
- Code quality improvements

3. Here's the code file by file:

Project Structure:
=================
../InstAanlyst-AI/InstAnalyst-AI\backend\scripts\migrate-database.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\app.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\server.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\config.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\database.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\gemini.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\logger.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\auth.controller.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\Controller.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\gapController.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\stakeholderController.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\transcriptController.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\userController.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\authMiddleware.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\dbHealthCheck.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\error.middleware.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\errorHandler.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\validation.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\commentModel.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\gapModel.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\requirementModel.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\transcriptModel.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\userModel.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\auth.routes.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\gaproutes.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\requirementRoutes.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\stakeholderRoutes.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\transcriptRoutes.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\userRoutes.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\geminiService.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\nlpService.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\requirementService.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\speechService.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\utils\asyncHandler.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\utils\databaseUtils.js
../InstAanlyst-AI/InstAnalyst-AI\backend\src\utils\idGenerator.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\.eslintrc.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\vue.config.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\main.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\plugins\vuetify.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\router\index.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\api.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\authService.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\gapService.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\requirementsService.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\stakeholderService.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\transcriptsService.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\index.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\activity.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\auth.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\gaps.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\notifications.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\requirements.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\stakeholders.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\transcripts.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\user.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\utils\formatters.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\utils\notifications.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\utils\validators.js
../InstAanlyst-AI/InstAnalyst-AI\frontend\src\assets\css\main.css



File: ../InstAanlyst-AI/InstAnalyst-AI\backend\scripts\migrate-database.js
==========================================================================

Chunk 1/1:
```
const fs = require('fs');
const path = require('path');
const { getPool } = require('../src/config/database');
const logger = require('../src/config/logger');

// Load environment variables
require('dotenv').config();

async function runSqlScript(pool, scriptPath) {
  const scriptContent = fs.readFileSync(scriptPath, 'utf8');
  
  // Split script into individual commands (by GO statements)
  const commands = scriptContent.split(/^\s*GO\s*$/m);
  
  for (const command of commands) {
    const trimmedCommand = command.trim();
    if (trimmedCommand) {
      try {
        await pool.request().batch(trimmedCommand);
        logger.info(`Executed SQL batch from ${path.basename(scriptPath)}`);
      } catch (err) {
        logger.error(`Error executing SQL from ${path.basename(scriptPath)}:`, err);
        throw err;
      }
    }
  }
}

async function migrateDatabase() {
  let pool;
  
  try {
    logger.info('Starting database migration...');
    
    // Get database connection pool
    pool = await getPool();
    
    // Schema creation
    const schemaScriptPath = path.join(__dirname, '../../db-schema.sql');
    await runSqlScript(pool, schemaScriptPath);
    logger.info('Database schema created successfully');
    
    // Seed data
    const seedScriptPath = path.join(__dirname, '../../db-seed.sql');
    await runSqlScript(pool, seedScriptPath);
    logger.info('Seed data inserted successfully');
    
    logger.info('Database migration completed successfully');
  } catch (error) {
    logger.error('Database migration failed:', error);
    process.exit(1);
  }
}

// Run the migration
migrateDatabase();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\app.js
=========================================================

Chunk 1/1:
```
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const { errorHandler } = require('./middleware/errorHandler');

// Import routes
const transcriptRoutes = require('./routes/transcriptRoutes');
const requirementRoutes = require('./routes/requirementRoutes');
const gapRoutes = require('./routes/gapRoutes');
const stakeholderRoutes = require('./routes/stakeholderRoutes');
const userRoutes = require('./routes/userRoutes');

// Initialize Express app
const app = express();

// Middleware
app.use(helmet());  // Security headers
app.use(cors());    // CORS support
app.use(express.json({ limit: '10mb' }));  // Body parsing
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
app.use(morgan('dev'));  // Logging

// API routes
const apiBasePath = process.env.API_BASE_URL || '/api';
app.use(`${apiBasePath}/transcripts`, transcriptRoutes);
app.use(`${apiBasePath}/requirements`, requirementRoutes);
app.use(`${apiBasePath}/gaps`, gapRoutes);
app.use(`${apiBasePath}/stakeholders`, stakeholderRoutes);
app.use(`${apiBasePath}/users`, userRoutes);

// Health check endpoint
app.get(`${apiBasePath}/health`, (req, res) => {
  res.status(200).json({ status: 'ok', timestamp: new Date().toISOString() });
});

// 404 handler
app.use((req, res, next) => {
  res.status(404).json({
    success: false,
    message: `Route not found: ${req.originalUrl}`
  });
});

// Error handler middleware
app.use(errorHandler);

module.exports = app;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\server.js
============================================================

Chunk 1/1:
```
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const authRoutes = require('./routes/auth.routes');
const errorHandler = require('./middleware/error.middleware');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/auth', authRoutes);

// Error handling
app.use(errorHandler);

// Health check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\config.js
===================================================================

Chunk 1/1:
```
require('dotenv').config();

module.exports = {
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || 'development',
  dbConfig: {
    server: process.env.DB_SERVER || 'localhost',
    database: process.env.DB_NAME || 'InstAnalyst'
  }
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\database.js
=====================================================================

Chunk 1/1:
```
const sql = require('mssql/msnodesqlv8');

const config = {
  server: process.env.DB_SERVER || 'localhost',
  database: process.env.DB_NAME || 'InstAnalyst',
  driver: 'msnodesqlv8',
  options: {
    trustedConnection: true,
    trustServerCertificate: true
  }
};

// Create a pool connection
let pool = null;

async function connectDB() {
  try {
    if (pool) {
      return pool;
    }

    pool = await new sql.ConnectionPool(config).connect();
    console.log('Connected to SQL Server successfully!');
    return pool;
  } catch (err) {
    console.error('Database connection failed:', err);
    throw err;
  }
}

// Helper function to execute queries
async function executeQuery(query, params = []) {
  try {
    const connection = await connectDB();
    const request = connection.request();

    // Add parameters if they exist
    params.forEach(param => {
      request.input(param.name, param.type, param.value);
    });

    const result = await request.query(query);
    return result;
  } catch (err) {
    console.error('Query execution failed:', err);
    throw err;
  }
}

module.exports = {
  sql,
  connectDB,
  executeQuery
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\gemini.js
===================================================================

Chunk 1/1:
```
const { GoogleGenerativeAI } = require('@google/generative-ai');
const logger = require('./logger');

// Initialize Google Generative AI client
let genAI = null;
let model = null;

// Get Gemini model
const getModel = () => {
  try {
    if (!genAI) {
      genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
    }
    
    if (!model) {
      model = genAI.getGenerativeModel({ model: 'gemini-1.5-pro' });
    }
    
    return model;
  } catch (error) {
    logger.error('Error initializing Gemini model:', error);
    throw new Error('Failed to initialize Gemini model');
  }
};

// Test Gemini connection
const testConnection = async () => {
  try {
    const model = getModel();
    const result = await model.generateContent('Test connection');
    return true;
  } catch (error) {
    logger.error('Error testing Gemini connection:', error);
    return false;
  }
};

module.exports = {
  getModel,
  testConnection
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\config\logger.js
===================================================================

Chunk 1/1:
```
const winston = require('winston');

// Define log format
const logFormat = winston.format.combine(
  winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
  winston.format.errors({ stack: true }),
  winston.format.splat(),
  winston.format.json()
);

// Create Winston logger
const logger = winston.createLogger({
  level: process.env.NODE_ENV === 'production' ? 'info' : 'debug',
  format: logFormat,
  defaultMeta: { service: 'transcript-requirements-api' },
  transports: [
    // Write to console in development
    process.env.NODE_ENV !== 'production' 
      ? new winston.transports.Console({
          format: winston.format.combine(
            winston.format.colorize(),
            winston.format.simple()
          )
        })
      : null,
    
    // Write all logs to files
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' })
  ].filter(Boolean)
});

module.exports = logger;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\auth.controller.js
=================================================================================

Chunk 1/1:
```
/* eslint-disable */
const jwt = require('jsonwebtoken');

// Mock user data
const MOCK_USER = {
  id: 1,
  email: 'demo@example.com',
  firstName: 'Demo',
  lastName: 'User',
  role: 'admin'
};

class AuthController {
  async login(req, res) {
    try {
      // Generate JWT token
      const token = jwt.sign(
        { 
          userId: MOCK_USER.id,
          email: MOCK_USER.email,
          role: MOCK_USER.role
        },
        process.env.JWT_SECRET || 'your-secret-key',
        { expiresIn: '24h' }
      );

      // Return success response with token and user data
      return res.status(200).json({
        success: true,
        message: 'Login successful',
        token,
        user: {
          id: MOCK_USER.id,
          email: MOCK_USER.email,
          firstName: MOCK_USER.firstName,
          lastName: MOCK_USER.lastName,
          role: MOCK_USER.role
        }
      });
    } catch (error) {
      console.error('Login error:', error);
      return res.status(200).json({
        success: true,
        message: 'Login successful (error handled)',
        token: 'mock-token',
        user: MOCK_USER
      });
    }
  }

  async register(req, res) {
    try {
      // Always return success with mock user
      return res.status(201).json({
        success: true,
        message: 'Registration successful',
        user: MOCK_USER
      });
    } catch (error) {
      console.error('Registration error:', error);
      return res.status(201).json({
        success: true,
        message: 'Registration successful (error handled)',
        user: MOCK_USER
      });
    }
  }

  async logout(req, res) {
    return res.status(200).json({
      success: true,
      message: 'Logout successful'
    });
  }

  async verifyToken(req, res) {
    return res.status(200).json({
      success: true,
      user: MOCK_USER
    });
  }
}

module.exports = new AuthController();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\Controller.js
============================================================================

Chunk 1/2:
```
const requirementModel = require('../models/requirementModel');
const gapModel = require('../models/gapModel');
const asyncHandler = require('../utils/asyncHandler');
const logger = require('../config/logger');

// @desc    Get all requirements
// @route   GET /api/requirements
// @access  Private
const getRequirements = asyncHandler(async (req, res) => {
  // Extract filters from query params
  const filters = {
    status: req.query.status,
    priority: req.query.priority,
    type: req.query.type,
    search: req.query.search,
    transcriptId: req.query.transcriptId,
    sortBy: req.query.sortBy,
    sortDirection: req.query.sortDirection
  };
  
  const requirements = await requirementModel.getAll(filters);
  
  res.status(200).json({
    success: true,
    count: requirements.length,
    data: requirements
  });
});

// @desc    Get single requirement
// @route   GET /api/requirements/:id
// @access  Private
const getRequirementById = asyncHandler(async (req, res) => {
  const requirement = await requirementModel.getById(req.params.id);
  
  if (!requirement) {
    return res.status(404).json({
      success: false,
      message: 'Requirement not found'
    });
  }
  
  res.status(200).json({
    success: true,
    data: requirement
  });
});

// @desc    Create new requirement
// @route   POST /api/requirements
// @access  Private
const createRequirement = asyncHandler(async (req, res) => {
  // Add user to requirement data
  req.body.CreatedBy = req.user.id;
  
  const requirementId = await requirementModel.create(req.body);
  
  res.status(201).json({
    success: true,
    data: { 
      RequirementID: requirementId,
      message: 'Requirement created successfully'
    }
  });
});

// @desc    Update requirement
// @route   PUT /api/requirements/:id
// @access  Private
const updateRequirement = asyncHandler(async (req, res) => {
  let requirement = await requirementModel.getById(req.params.id);
  
  if (!requirement) {
    return res.status(404).json({
      success: false,
      message: 'Requirement not found'
    });
  }
  
  // Add user who updated
  req.body.UpdatedBy = req.user.id;
  
  await requirementModel.update(req.params.id, req.body);
  
  // Get updated requirement
  requirement = await requirementModel.getById(req.params.id);
  
  res.status(200).json({
    success: true,
    data: requirement
  });
});

// @desc    Update requirement status
// @route   PATCH /api/requirements/:id/status
// @access  Private
const updateRequirementStatus = asyncHandler(async (req, res) => {
  const { status } = req.body;
  
  if (!status) {
    return res.status(400).json({
      success: false,
      message: 'Please provide a status'
    });
  }
  
  const requirement = await requirementModel.getById(req.params.id);
  
  if (!requirement) {
    return res.status(404).json({
      success: false,
      message: 'Requirement not found'
    });
  }
  
  await requirementModel.updateStatus(req.params.id, status, req.user.id);
  
  res.status(200).json({
    success: true,
    data: { 
      RequirementID: req.params.id,
      status,
      message: 'Status updated successfully'
    }
  });
});

// @desc    Delete requirement
// @route   DELETE /api/requirements/:id
// @access  Private
const deleteRequirement = asyncHandler(async (req, res) => {
  const requirement = await requirementModel.getById(req.params.id);
  
  if (!requirement) {
    return res.status(404).json({
      success: false,
      message: 'Requirement not found'
    });
  }
  
  // Check if requirement has associated gaps
  const gaps = await gapModel.getByRequirementId(req.params.id);
  
  if (gaps.length > 0) {
    return res.status(400).json({
      success: false,
      message: 'Cannot delete requirement with associated gaps. Please remove gaps first.'
    });
  }
  
  await requirementModel.remove(req.params.id);
  
  res.status(200).json({
    success: true,
    data: {}
  });
});

// @desc    Get gaps for a requirement
// @route   GET /api/req
```


Chunk 2/2:
```
uirements/:id/gaps
// @access  Private
const getRequirementGaps = asyncHandler(async (req, res) => {
  const requirement = await requirementModel.getById(req.params.id);
  
  if (!requirement) {
    return res.status(404).json({
      success: false,
      message: 'Requirement not found'
    });
  }
  
  const gaps = await gapModel.getByRequirementId(req.params.id);
  
  res.status(200).json({
    success: true,
    count: gaps.length,
    data: gaps
  });
});

module.exports = {
  getRequirements,
  getRequirementById,
  createRequirement,
  updateRequirement,
  updateRequirementStatus,
  deleteRequirement,
  getRequirementGaps
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\gapController.js
===============================================================================

Chunk 1/1:
```
const gapModel = require('../models/gapModel');
const requirementModel = require('../models/requirementModel');
const asyncHandler = require('../utils/asyncHandler');
const logger = require('../config/logger');

// @desc    Get all gaps
// @route   GET /api/gaps
// @access  Private
const getGaps = asyncHandler(async (req, res) => {
  // Extract filters from query params
  const filters = {
    status: req.query.status,
    severity: req.query.severity,
    requirementId: req.query.requirementId,
    search: req.query.search,
    sortBy: req.query.sortBy,
    sortDirection: req.query.sortDirection
  };
  
  const gaps = await gapModel.getAll(filters);
  
  res.status(200).json({
    success: true,
    count: gaps.length,
    data: gaps
  });
});

// @desc    Get single gap
// @route   GET /api/gaps/:id
// @access  Private
const getGapById = asyncHandler(async (req, res) => {
  const gap = await gapModel.getById(req.params.id);
  
  if (!gap) {
    return res.status(404).json({
      success: false,
      message: 'Gap not found'
    });
  }
  
  res.status(200).json({
    success: true,
    data: gap
  });
});

// @desc    Create new gap
// @route   POST /api/gaps
// @access  Private
const createGap = asyncHandler(async (req, res) => {
  // Check if related requirement exists if provided
  if (req.body.RelatedRequirementID) {
    const requirement = await requirementModel.getById(req.body.RelatedRequirementID);
    
    if (!requirement) {
      return res.status(404).json({
        success: false,
        message: 'Related requirement not found'
      });
    }
  }
  
  // Add user to gap data
  req.body.CreatedBy = req.user.id;
  
  const gapId = await gapModel.create(req.body);
  
  res.status(201).json({
    success: true,
    data: { 
      GapID: gapId,
      message: 'Gap created successfully'
    }
  });
});

// @desc    Update gap
// @route   PUT /api/gaps/:id
// @access  Private
const updateGap = asyncHandler(async (req, res) => {
  let gap = await gapModel.getById(req.params.id);
  
  if (!gap) {
    return res.status(404).json({
      success: false,
      message: 'Gap not found'
    });
  }
  
  // Check if related requirement exists if provided
  if (req.body.RelatedRequirementID) {
    const requirement = await requirementModel.getById(req.body.RelatedRequirementID);
    
    if (!requirement) {
      return res.status(404).json({
        success: false,
        message: 'Related requirement not found'
      });
    }
  }
  
  // Add user who updated
  req.body.UpdatedBy = req.user.id;
  
  await gapModel.update(req.params.id, req.body);
  
  // Get updated gap
  gap = await gapModel.getById(req.params.id);
  
  res.status(200).json({
    success: true,
    data: gap
  });
});

// @desc    Update gap status
// @route   PATCH /api/gaps/:id/status
// @access  Private
const updateGapStatus = asyncHandler(async (req, res) => {
  const { status } = req.body;
  
  if (!status) {
    return res.status(400).json({
      success: false,
      message: 'Please provide a status'
    });
  }
  
  const gap = await gapModel.getById(req.params.id);
  
  if (!gap) {
    return res.status(404).json({
      success: false,
      message: 'Gap not found'
    });
  }
  
  await gapModel.updateStatus(req.params.id, status, req.user.id);
  
  res.status(200).json({
    success: true,
    data: { 
      GapID: req.params.id,
      status,
      message: 'Status updated successfully'
    }
  });
});

// @desc    Delete gap
// @route   DELETE /api/gaps/:id
// @access  Private
const deleteGap = asyncHandler(async (req, res) => {
  const gap = await gapModel.getById(req.params.id);
  
  if (!gap) {
    return res.status(404).json({
      success: false,
      message: 'Gap not found'
    });
  }
  
  await gapModel.remove(req.params.id);
  
  res.status(200).json({
    success: true,
    data: {}
  });
});

module.exports = {
  getGaps,
  getGapById,
  createGap,
  updateGap,
  updateGapStatus,
  deleteGap
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\stakeholderController.js
=======================================================================================

Chunk 1/1:
```
const stakeholderModel = require('../models/stakeholderModel');
const asyncHandler = require('../utils/asyncHandler');
const logger = require('../config/logger');

// @desc    Get all stakeholders
// @route   GET /api/stakeholders
// @access  Private
const getStakeholders = asyncHandler(async (req, res) => {
  // Extract filters from query params
  const filters = {
    role: req.query.role,
    influenceLevel: req.query.influenceLevel,
    interestLevel: req.query.interestLevel,
    search: req.query.search,
    sortBy: req.query.sortBy,
    sortDirection: req.query.sortDirection
  };
  
  const stakeholders = await stakeholderModel.getAll(filters);
  
  res.status(200).json({
    success: true,
    count: stakeholders.length,
    data: stakeholders
  });
});

// @desc    Get single stakeholder
// @route   GET /api/stakeholders/:id
// @access  Private
const getStakeholderById = asyncHandler(async (req, res) => {
  const stakeholder = await stakeholderModel.getById(req.params.id);
  
  if (!stakeholder) {
    return res.status(404).json({
      success: false,
      message: 'Stakeholder not found'
    });
  }
  
  res.status(200).json({
    success: true,
    data: stakeholder
  });
});

// @desc    Create new stakeholder
// @route   POST /api/stakeholders
// @access  Private
const createStakeholder = asyncHandler(async (req, res) => {
  // Add user to stakeholder data
  req.body.CreatedBy = req.user.id;
  
  const stakeholderId = await stakeholderModel.create(req.body);
  
  res.status(201).json({
    success: true,
    data: { 
      StakeholderID: stakeholderId,
      message: 'Stakeholder created successfully'
    }
  });
});

// @desc    Update stakeholder
// @route   PUT /api/stakeholders/:id
// @access  Private
const updateStakeholder = asyncHandler(async (req, res) => {
  let stakeholder = await stakeholderModel.getById(req.params.id);
  
  if (!stakeholder) {
    return res.status(404).json({
      success: false,
      message: 'Stakeholder not found'
    });
  }
  
  // Add user who updated
  req.body.UpdatedBy = req.user.id;
  
  await stakeholderModel.update(req.params.id, req.body);
  
  // Get updated stakeholder
  stakeholder = await stakeholderModel.getById(req.params.id);
  
  res.status(200).json({
    success: true,
    data: stakeholder
  });
});

// @desc    Delete stakeholder
// @route   DELETE /api/stakeholders/:id
// @access  Private
const deleteStakeholder = asyncHandler(async (req, res) => {
  const stakeholder = await stakeholderModel.getById(req.params.id);
  
  if (!stakeholder) {
    return res.status(404).json({
      success: false,
      message: 'Stakeholder not found'
    });
  }
  
  await stakeholderModel.remove(req.params.id);
  
  res.status(200).json({
    success: true,
    data: {}
  });
});

// @desc    Get stakeholder's associated requirements
// @route   GET /api/stakeholders/:id/requirements
// @access  Private
const getStakeholderRequirements = asyncHandler(async (req, res) => {
  const stakeholder = await stakeholderModel.getById(req.params.id);
  
  if (!stakeholder) {
    return res.status(404).json({
      success: false,
      message: 'Stakeholder not found'
    });
  }
  
  const requirements = await stakeholderModel.getRequirements(req.params.id);
  
  res.status(200).json({
    success: true,
    count: requirements.length,
    data: requirements
  });
});

module.exports = {
  getStakeholders,
  getStakeholderById,
  createStakeholder,
  updateStakeholder,
  deleteStakeholder,
  getStakeholderRequirements
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\transcriptController.js
======================================================================================

Chunk 1/2:
```
const transcriptModel = require('../models/transcriptModel');
const requirementModel = require('../models/requirementModel');
const gapModel = require('../models/gapModel');
const stakeholderModel = require('../models/stakeholderModel');
const geminiService = require('../services/geminiService');
const logger = require('../config/logger');
const asyncHandler = require('../utils/asyncHandler');

// @desc    Upload and process a new transcript
// @route   POST /api/transcripts
// @access  Private
const uploadTranscript = asyncHandler(async (req, res) => {
  const { title, content, meetingDate } = req.body;
  
  // Validate required fields
  if (!title || !content || !meetingDate) {
    return res.status(400).json({ 
      success: false, 
      message: 'Please provide title, content, and meeting date' 
    });
  }

  // Create transcript record
  const transcriptData = {
    title,
    content,
    meetingDate,
    uploadedBy: req.user.id
  };
  
  const transcriptId = await transcriptModel.create(transcriptData);
  
  // Start async processing (don't await)
  processTranscript(transcriptId, content, req.user.id);
  
  res.status(201).json({
    success: true,
    data: { 
      transcriptId,
      message: 'Transcript uploaded and being processed'
    }
  });
});

// Process transcript using Gemini AI (async)
const processTranscript = async (transcriptId, content, userId) => {
  try {
    // Update status to processing
    await transcriptModel.updateStatus(transcriptId, 'Processing');
    
    // Analyze transcript with Gemini
    const analysis = await geminiService.analyzeTranscript(content);
    
    // Process requirements
    if (analysis.requirements && Array.isArray(analysis.requirements)) {
      for (const req of analysis.requirements) {
        await requirementModel.create({
          ...req,
          TranscriptID: transcriptId,
          CreatedBy: userId
        });
      }
    }
    
    // Process gaps
    if (analysis.gaps && Array.isArray(analysis.gaps)) {
      for (const gap of analysis.gaps) {
        await gapModel.create({
          ...gap,
          CreatedBy: userId
        });
      }
    }
    
    // Process stakeholders
    if (analysis.stakeholders && Array.isArray(analysis.stakeholders)) {
      for (const stakeholder of analysis.stakeholders) {
        await stakeholderModel.create({
          ...stakeholder,
          CreatedBy: userId
        });
      }
    }
    
    // Update status to completed
    await transcriptModel.updateStatus(transcriptId, 'Completed');
    logger.info(`Transcript ${transcriptId} processed successfully`);
  } catch (error) {
    logger.error(`Error processing transcript ${transcriptId}:`, error);
    await transcriptModel.updateStatus(
      transcriptId, 
      'Failed', 
      error.message || 'Unknown error during processing'
    );
  }
};

// @desc    Get all transcripts
// @route   GET /api/transcripts
// @access  Private
const getTranscripts = asyncHandler(async (req, res) => {
  const transcripts = await transcriptModel.getAll();
  
  res.status(200).json({
    success: true,
    count: transcripts.length,
    data: transcripts
  });
});

// @desc    Get single transcript
// @route   GET /api/transcripts/:id
// @access  Private
const getTranscriptById = asyncHandler(async (req, res) => {
  const transcript = await transcriptModel.getById(req.params.id);
  
  if (!transcript) {
    return res.status(404).json({
      success: false,
      message: 'Transcript not found'
    });
  }
  
  res.status(200).json({
    success: true,
    data: transcript
  });
});

// @desc    Get requirements generated from transcript
// @route   GET /api/transcripts/:id/requirements
// @access  Private
const getTranscriptRequirements = asyncHandler(async (req, res) => {
  const transcript = await transcriptModel.getById(req.params.id);
  
  if (!transcript) {
    return res.status(404).json({
      success: false,
      message: 'Transcript not found'
    });
  }
  
  const requi
```


Chunk 2/2:
```
rements = await requirementModel.getByTranscriptId(req.params.id);
  
  res.status(200).json({
    success: true,
    count: requirements.length,
    data: requirements
  });
});

// @desc    Delete transcript
// @route   DELETE /api/transcripts/:id
// @access  Private
const deleteTranscript = asyncHandler(async (req, res) => {
  const transcript = await transcriptModel.getById(req.params.id);
  
  if (!transcript) {
    return res.status(404).json({
      success: false,
      message: 'Transcript not found'
    });
  }
  
  await transcriptModel.remove(req.params.id);
  
  res.status(200).json({
    success: true,
    data: {}
  });
});

module.exports = {
  uploadTranscript,
  getTranscripts,
  getTranscriptById,
  getTranscriptRequirements,
  deleteTranscript
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\controllers\userController.js
================================================================================

Chunk 1/2:
```
const userModel = require('../models/userModel');
const asyncHandler = require('../utils/asyncHandler');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const logger = require('../config/logger');

// Helper: Generate JWT token
const generateToken = (id) => {
  return jwt.sign({ id }, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRES_IN || '1d'
  });
};

// @desc    Register new user
// @route   POST /api/users/register
// @access  Public
const registerUser = asyncHandler(async (req, res) => {
  const { firstName, lastName, email, password, role } = req.body;
  
  // Check if user already exists
  const userExists = await userModel.getByEmail(email);
  
  if (userExists) {
    return res.status(400).json({
      success: false,
      message: 'User already exists'
    });
  }
  
  // Hash password
  const salt = await bcrypt.genSalt(10);
  const hashedPassword = await bcrypt.hash(password, salt);
  
  // Create user
  const userId = await userModel.create({
    FirstName: firstName,
    LastName: lastName,
    Email: email,
    PasswordHash: hashedPassword,
    Role: role || 'User'
  });
  
  if (userId) {
    const user = await userModel.getById(userId);
    
    res.status(201).json({
      success: true,
      data: {
        id: user.UserID,
        firstName: user.FirstName,
        lastName: user.LastName,
        email: user.Email,
        role: user.Role,
        token: generateToken(user.UserID)
      }
    });
  } else {
    res.status(400).json({
      success: false,
      message: 'Invalid user data'
    });
  }
});

// @desc    Authenticate user (login)
// @route   POST /api/users/login
// @access  Public
const loginUser = asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  
  // Check for user email
  const user = await userModel.getByEmail(email);
  
  if (!user) {
    return res.status(401).json({
      success: false,
      message: 'Invalid credentials'
    });
  }
  
  // Check if user is active
  if (!user.IsActive) {
    return res.status(401).json({
      success: false,
      message: 'Account is disabled'
    });
  }
  
  // Check password
  const isMatch = await bcrypt.compare(password, user.PasswordHash);
  
  if (!isMatch) {
    return res.status(401).json({
      success: false,
      message: 'Invalid credentials'
    });
  }
  
  // Update last login date
  await userModel.updateLastLogin(user.UserID);
  
  res.status(200).json({
    success: true,
    data: {
      id: user.UserID,
      firstName: user.FirstName,
      lastName: user.LastName,
      email: user.Email,
      role: user.Role,
      token: generateToken(user.UserID)
    }
  });
});

// @desc    Get current user profile
// @route   GET /api/users/me
// @access  Private
const getMe = asyncHandler(async (req, res) => {
  const user = await userModel.getById(req.user.id);
  
  if (!user) {
    return res.status(404).json({
      success: false,
      message: 'User not found'
    });
  }
  
  res.status(200).json({
    success: true,
    data: {
      id: user.UserID,
      firstName: user.FirstName,
      lastName: user.LastName,
      email: user.Email,
      role: user.Role,
      department: user.Department,
      avatar: user.Avatar,
      createdDate: user.CreatedDate,
      lastLoginDate: user.LastLoginDate
    }
  });
});

// @desc    Update user profile
// @route   PUT /api/users/me
// @access  Private
const updateProfile = asyncHandler(async (req, res) => {
  const { firstName, lastName, email, department, avatar, currentPassword, newPassword } = req.body;
  
  const user = await userModel.getById(req.user.id);
  
  if (!user) {
    return res.status(404).json({
      success: false,
      message: 'User not found'
    });
  }
  
  // If user wants to change password, verify current password
  if (newPassword) {
    if (!currentPassword) {
      return res.status(400).json({
        success: false,
        message: 'Current password is required to set new passw
```


Chunk 2/2:
```
ord'
      });
    }
    
    const isMatch = await bcrypt.compare(currentPassword, user.PasswordHash);
    
    if (!isMatch) {
      return res.status(401).json({
        success: false,
        message: 'Current password is incorrect'
      });
    }
    
    // Hash new password
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(newPassword, salt);
    
    await userModel.updatePassword(req.user.id, hashedPassword);
  }
  
  // Update profile data
  const updateData = {
    FirstName: firstName || user.FirstName,
    LastName: lastName || user.LastName,
    Email: email || user.Email,
    Department: department !== undefined ? department : user.Department,
    Avatar: avatar !== undefined ? avatar : user.Avatar
  };
  
  await userModel.updateProfile(req.user.id, updateData);
  
  // Get updated user
  const updatedUser = await userModel.getById(req.user.id);
  
  res.status(200).json({
    success: true,
    data: {
      id: updatedUser.UserID,
      firstName: updatedUser.FirstName,
      lastName: updatedUser.LastName,
      email: updatedUser.Email,
      role: updatedUser.Role,
      department: updatedUser.Department,
      avatar: updatedUser.Avatar
    }
  });
});

// @desc    Get all users (admin only)
// @route   GET /api/users
// @access  Private/Admin
const getUsers = asyncHandler(async (req, res) => {
  // Check if user is admin
  if (req.user.role !== 'Admin') {
    return res.status(403).json({
      success: false,
      message: 'Not authorized to access this resource'
    });
  }
  
  const users = await userModel.getAll();
  
  res.status(200).json({
    success: true,
    count: users.length,
    data: users
  });
});

module.exports = {
  registerUser,
  loginUser,
  getMe,
  updateProfile,
  getUsers
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\authMiddleware.js
===============================================================================

Chunk 1/1:
```
/* eslint-disable */
const jwt = require('jsonwebtoken');

// Mock user for authentication bypass
const MOCK_USER = {
  id: 1,
  email: 'demo@example.com',
  role: 'admin'
};

const authMiddleware = (req, res, next) => {
  try {
    // Always authenticate successfully
    req.user = MOCK_USER;
    next();
  } catch (error) {
    console.error('Auth middleware error:', error);
    // Still allow the request to proceed
    req.user = MOCK_USER;
    next();
  }
};

module.exports = authMiddleware;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\dbHealthCheck.js
==============================================================================

Chunk 1/1:
```
const { getPool } = require('../config/database');
const logger = require('../config/logger');

/**
 * Middleware to check database connectivity
 */
const dbHealthCheck = async (req, res, next) => {
  try {
    const pool = await getPool();
    const result = await pool.request().query('SELECT 1 as dbConnected');
    
    if (result.recordset[0].dbConnected === 1) {
      next();
    } else {
      logger.error('Database health check failed: unexpected response');
      res.status(503).json({ message: 'Database service unavailable' });
    }
  } catch (error) {
    logger.error('Database health check failed:', error);
    res.status(503).json({ message: 'Database service unavailable' });
  }
};

module.exports = dbHealthCheck;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\error.middleware.js
=================================================================================

Chunk 1/1:
```
/* eslint-disable */
const errorHandler = (err, req, res, next) => {
    console.error('Error:', err);
    
    // Always return success response
    return res.status(200).json({
      success: true,
      message: 'Operation successful (error handled)',
      user: {
        id: 1,
        email: 'demo@example.com',
        firstName: 'Demo',
        lastName: 'User',
        role: 'admin'
      }
    });
  };
  
  module.exports = errorHandler;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\errorHandler.js
=============================================================================

Chunk 1/1:
```
const logger = require('../config/logger');

/**
 * Custom error class for API errors with status code
 */
class ApiError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}

/**
 * Global error handler middleware for Express
 */
const errorHandler = (err, req, res, next) => {
  let error = { ...err };
  error.message = err.message;
  
  // Log error
  logger.error(`${req.method} ${req.url} - Error:`, {
    error: err.message,
    stack: process.env.NODE_ENV === 'development' ? err.stack : 'Hidden in production',
    statusCode: err.statusCode || 500
  });
  
  // SQL Server error handling
  if (err.name === 'RequestError' || err.code === 'EREQUEST') {
    const message = 'Database query error';
    error = new ApiError(message, 500);
  }
  
  // Handling JWT errors
  if (err.name === 'JsonWebTokenError') {
    const message = 'Invalid token';
    error = new ApiError(message, 401);
  }
  
  if (err.name === 'TokenExpiredError') {
    const message = 'Token expired';
    error = new ApiError(message, 401);
  }
  
  // Send response
  res.status(error.statusCode || 500).json({
    success: false,
    message: error.message || 'Server Error',
    stack: process.env.NODE_ENV === 'development' ? err.stack : undefined
  });
};

module.exports = {
  errorHandler,
  ApiError
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\middleware\validation.js
===========================================================================

Chunk 1/2:
```
const { body, param, query, validationResult } = require('express-validator');
const logger = require('../config/logger');

/**
 * Middleware to check validation results
 */
const validate = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    logger.warn(`Validation error in ${req.method} ${req.originalUrl}:`, errors.array());
    return res.status(400).json({
      success: false,
      errors: errors.array()
    });
  }
  next();
};

/**
 * Validation rules for transcript endpoints
 */
const transcriptValidation = {
  create: [
    body('title')
      .notEmpty().withMessage('Title is required')
      .isLength({ max: 255 }).withMessage('Title cannot exceed 255 characters'),
    body('content')
      .notEmpty().withMessage('Content is required'),
    body('meetingDate')
      .notEmpty().withMessage('Meeting date is required')
      .isISO8601().withMessage('Meeting date must be a valid date'),
    validate
  ]
};

/**
 * Validation rules for requirement endpoints
 */
const requirementValidation = {
  create: [
    body('RequirementTitle')
      .notEmpty().withMessage('Requirement title is required')
      .isLength({ max: 255 }).withMessage('Title cannot exceed 255 characters'),
    body('RequirementDescription')
      .notEmpty().withMessage('Description is required'),
    body('RequirementType')
      .optional()
      .isIn(['Functional', 'Non-Functional', 'Technical', 'Business', 'User Interface', 'Security', 'Performance', 'Compliance'])
      .withMessage('Invalid requirement type'),
    body('Priority')
      .optional()
      .isIn(['High', 'Medium', 'Low'])
      .withMessage('Priority must be High, Medium, or Low'),
    body('Status')
      .optional()
      .isIn(['Draft', 'In Progress', 'Reviewed', 'Approved', 'Implemented', 'Completed', 'On Hold', 'Rejected'])
      .withMessage('Invalid status'),
    validate
  ],
  update: [
    param('id')
      .notEmpty().withMessage('Requirement ID is required'),
    body('RequirementTitle')
      .optional()
      .isLength({ max: 255 }).withMessage('Title cannot exceed 255 characters'),
    body('RequirementType')
      .optional()
      .isIn(['Functional', 'Non-Functional', 'Technical', 'Business', 'User Interface', 'Security', 'Performance', 'Compliance'])
      .withMessage('Invalid requirement type'),
    body('Priority')
      .optional()
      .isIn(['High', 'Medium', 'Low'])
      .withMessage('Priority must be High, Medium, or Low'),
    body('Status')
      .optional()
      .isIn(['Draft', 'In Progress', 'Reviewed', 'Approved', 'Implemented', 'Completed', 'On Hold', 'Rejected'])
      .withMessage('Invalid status'),
    validate
  ],
  updateStatus: [
    param('id')
      .notEmpty().withMessage('Requirement ID is required'),
    body('status')
      .notEmpty().withMessage('Status is required')
      .isIn(['Draft', 'In Progress', 'Reviewed', 'Approved', 'Implemented', 'Completed', 'On Hold', 'Rejected'])
      .withMessage('Invalid status'),
    validate
  ]
};

/**
 * Validation rules for gap endpoints
 */
const gapValidation = {
  create: [
    body('GapDescription')
      .notEmpty().withMessage('Gap description is required'),
    body('GapSeverity')
      .optional()
      .isIn(['Critical', 'Major', 'Minor'])
      .withMessage('Severity must be Critical, Major, or Minor'),
    body('GapStatus')
      .optional()
      .isIn(['Open', 'Under Investigation', 'Resolved', 'Closed', 'Deferred', 'Won\'t Fix'])
      .withMessage('Invalid status'),
    body('RelatedRequirementID')
      .optional()
      .isString().withMessage('Related requirement ID must be a string'),
    validate
  ],
  update: [
    param('id')
      .notEmpty().withMessage('Gap ID is required'),
    body('GapSeverity')
      .optional()
      .isIn(['Critical', 'Major', 'Minor'])
      .withMessage('Severity must be Critical, Major, or Minor'),
    body('GapStatus')
      .optional()
      .isIn(['Open', 'Under Investigation', 'Resolved', 'Clo
```


Chunk 2/2:
```
sed', 'Deferred', 'Won\'t Fix'])
      .withMessage('Invalid status'),
    validate
  ],
  updateStatus: [
    param('id')
      .notEmpty().withMessage('Gap ID is required'),
    body('status')
      .notEmpty().withMessage('Status is required')
      .isIn(['Open', 'Under Investigation', 'Resolved', 'Closed', 'Deferred', 'Won\'t Fix'])
      .withMessage('Invalid status'),
    validate
  ]
};

/**
 * Validation rules for stakeholder endpoints
 */
const stakeholderValidation = {
  create: [
    body('StakeholderName')
      .notEmpty().withMessage('Stakeholder name is required')
      .isLength({ max: 100 }).withMessage('Name cannot exceed 100 characters'),
    body('StakeholderRole')
      .optional()
      .isLength({ max: 50 }).withMessage('Role cannot exceed 50 characters'),
    body('InfluenceLevel')
      .optional()
      .isIn(['Decision Maker', 'Influencer', 'Informed'])
      .withMessage('Influence level must be Decision Maker, Influencer, or Informed'),
    body('InterestLevel')
      .optional()
      .isIn(['High', 'Medium', 'Low'])
      .withMessage('Interest level must be High, Medium, or Low'),
    validate
  ],
  update: [
    param('id')
      .notEmpty().withMessage('Stakeholder ID is required'),
    body('StakeholderName')
      .optional()
      .isLength({ max: 100 }).withMessage('Name cannot exceed 100 characters'),
    body('StakeholderRole')
      .optional()
      .isLength({ max: 50 }).withMessage('Role cannot exceed 50 characters'),
    body('InfluenceLevel')
      .optional()
      .isIn(['Decision Maker', 'Influencer', 'Informed'])
      .withMessage('Influence level must be Decision Maker, Influencer, or Informed'),
    body('InterestLevel')
      .optional()
      .isIn(['High', 'Medium', 'Low'])
      .withMessage('Interest level must be High, Medium, or Low'),
    validate
  ]
};

/**
 * Validation rules for user endpoints
 */
const userValidation = {
  register: [
    body('firstName')
      .notEmpty().withMessage('First name is required')
      .isLength({ max: 50 }).withMessage('First name cannot exceed 50 characters'),
    body('lastName')
      .notEmpty().withMessage('Last name is required')
      .isLength({ max: 50 }).withMessage('Last name cannot exceed 50 characters'),
    body('email')
      .notEmpty().withMessage('Email is required')
      .isEmail().withMessage('Please provide a valid email')
      .normalizeEmail(),
    body('password')
      .notEmpty().withMessage('Password is required')
      .isLength({ min: 6 }).withMessage('Password must be at least 6 characters long'),
    body('role')
      .optional()
      .isIn(['Admin', 'Manager', 'User'])
      .withMessage('Role must be Admin, Manager, or User'),
    validate
  ],
  login: [
    body('email')
      .notEmpty().withMessage('Email is required')
      .isEmail().withMessage('Please provide a valid email')
      .normalizeEmail(),
    body('password')
      .notEmpty().withMessage('Password is required'),
    validate
  ],
  updateProfile: [
    body('firstName')
      .optional()
      .isLength({ max: 50 }).withMessage('First name cannot exceed 50 characters'),
    body('lastName')
      .optional()
      .isLength({ max: 50 }).withMessage('Last name cannot exceed 50 characters'),
    body('email')
      .optional()
      .isEmail().withMessage('Please provide a valid email')
      .normalizeEmail(),
    body('newPassword')
      .optional()
      .isLength({ min: 6 }).withMessage('New password must be at least 6 characters long'),
    body('currentPassword')
      .if(body('newPassword').exists())
      .notEmpty().withMessage('Current password is required to change password'),
    validate
  ]
};

module.exports = {
  validate,
  transcriptValidation,
  requirementValidation,
  gapValidation,
  stakeholderValidation,
  userValidation
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\commentModel.js
=========================================================================

Chunk 1/2:
```
const { getPool, sql } = require('../../config/database');
const logger = require('../../config/logger');

class CommentModel {
  async create(comment) {
    try {
      const pool = await getPool();
      
      // Generate comment ID
      const result = await pool.request()
        .query(`
          SELECT TOP 1 CommentID FROM Comments
          WHERE CommentID LIKE 'COM-%'
          ORDER BY CommentID DESC
        `);
      
      let nextId = 1;
      if (result.recordset.length > 0) {
        const lastId = result.recordset[0].CommentID;
        const lastNumber = parseInt(lastId.split('-')[1]);
        nextId = lastNumber + 1;
      }
      
      const commentId = `COM-${nextId.toString().padStart(6, '0')}`;
      
      // Insert comment
      await pool.request()
        .input('CommentID', sql.NVarChar(20), commentId)
        .input('CommentText', sql.NVarChar(sql.MAX), comment.CommentText)
        .input('CommentedBy', sql.NVarChar(100), comment.CommentedBy)
        .input('RequirementID', sql.NVarChar(20), comment.RequirementID)
        .input('GapID', sql.NVarChar(20), comment.GapID)
        .input('StakeholderID', sql.NVarChar(20), comment.StakeholderID)
        .input('ParentCommentID', sql.NVarChar(20), comment.ParentCommentID)
        .query(`
          INSERT INTO Comments (
            CommentID, CommentText, CommentDate, CommentedBy,
            RequirementID, GapID, StakeholderID, ParentCommentID
          )
          VALUES (
            @CommentID, @CommentText, GETDATE(), @CommentedBy,
            @RequirementID, @GapID, @StakeholderID, @ParentCommentID
          )
        `);
      
      // Add history if this is a requirement comment
      if (comment.RequirementID) {
        // We'll use the existing requirementModel for this, so just log
        logger.info(`Added comment ${commentId} to requirement ${comment.RequirementID}`);
      }
      
      return commentId;
    } catch (error) {
      logger.error('Error creating comment:', error);
      throw new Error(`Failed to create comment: ${error.message}`);
    }
  }

  async update(commentId, commentText, updatedBy) {
    try {
      const pool = await getPool();
      
      // Get the current comment to check permissions and track changes
      const currentComment = await this.getById(commentId);
      
      if (!currentComment) {
        throw new Error(`Comment with ID ${commentId} not found`);
      }
      
      // Only the original commenter should be able to edit it
      if (currentComment.CommentedBy !== updatedBy) {
        throw new Error('You can only edit your own comments');
      }
      
      // Update comment
      await pool.request()
        .input('CommentID', sql.NVarChar(20), commentId)
        .input('CommentText', sql.NVarChar(sql.MAX), commentText)
        .input('LastEditedBy', sql.NVarChar(100), updatedBy)
        .query(`
          UPDATE Comments
          SET CommentText = @CommentText,
              LastEdited = GETDATE(),
              LastEditedBy = @LastEditedBy,
              IsEdited = 1
          WHERE CommentID = @CommentID
        `);
      
      return commentId;
    } catch (error) {
      logger.error('Error updating comment:', error);
      throw new Error(`Failed to update comment: ${error.message}`);
    }
  }

  async delete(commentId, deletedBy) {
    try {
      const pool = await getPool();
      
      // Get the current comment to check permissions
      const currentComment = await this.getById(commentId);
      
      if (!currentComment) {
        throw new Error(`Comment with ID ${commentId} not found`);
      }
      
      // Only the original commenter should be able to delete it
      if (currentComment.CommentedBy !== deletedBy) {
        throw new Error('You can only delete your own comments');
      }
      
      // Delete comment
      await pool.request()
        .input('CommentID', sql.NVarChar(20), commentId)
        .query(`
          DELETE FROM Comments
          WHERE C
```


Chunk 2/2:
```
ommentID = @CommentID
        `);
      
      return true;
    } catch (error) {
      logger.error('Error deleting comment:', error);
      throw new Error(`Failed to delete comment: ${error.message}`);
    }
  }

  async getById(id) {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .input('CommentID', sql.NVarChar(20), id)
        .query(`
          SELECT * FROM Comments
          WHERE CommentID = @CommentID
        `);
      
      return result.recordset[0];
    } catch (error) {
      logger.error('Error fetching comment by ID:', error);
      throw new Error(`Failed to fetch comment: ${error.message}`);
    }
  }

  async getByRequirementId(requirementId) {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .input('RequirementID', sql.NVarChar(20), requirementId)
        .query(`
          SELECT c.*, u.FullName as CommenterName
          FROM Comments c
          LEFT JOIN Users u ON c.CommentedBy = u.UserID
          WHERE c.RequirementID = @RequirementID
          ORDER BY c.CommentDate ASC
        `);
      
      return result.recordset;
    } catch (error) {
      logger.error('Error fetching comments by requirement ID:', error);
      throw new Error(`Failed to fetch comments: ${error.message}`);
    }
  }

  async getByGapId(gapId) {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .input('GapID', sql.NVarChar(20), gapId)
        .query(`
          SELECT c.*, u.FullName as CommenterName
          FROM Comments c
          LEFT JOIN Users u ON c.CommentedBy = u.UserID
          WHERE c.GapID = @GapID
          ORDER BY c.CommentDate ASC
        `);
      
      return result.recordset;
    } catch (error) {
      logger.error('Error fetching comments by gap ID:', error);
      throw new Error(`Failed to fetch comments: ${error.message}`);
    }
  }

  async getReplies(parentCommentId) {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .input('ParentCommentID', sql.NVarChar(20), parentCommentId)
        .query(`
          SELECT c.*, u.FullName as CommenterName
          FROM Comments c
          LEFT JOIN Users u ON c.CommentedBy = u.UserID
          WHERE c.ParentCommentID = @ParentCommentID
          ORDER BY c.CommentDate ASC
        `);
      
      return result.recordset;
    } catch (error) {
      logger.error('Error fetching comment replies:', error);
      throw new Error(`Failed to fetch comment replies: ${error.message}`);
    }
  }
}

module.exports = new CommentModel();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\gapModel.js
=====================================================================

Chunk 1/1:
```
const { getPool, sql } = require('../config/database');
const logger = require('../config/logger');

// Generate unique GapID
const generateGapId = async () => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .query(`
        SELECT TOP 1 GapID FROM Gaps
        WHERE GapID LIKE 'GAP-%'
        ORDER BY GapID DESC
      `);
    
    let nextId = 1;
    if (result.recordset.length > 0) {
      const lastId = result.recordset[0].GapID;
      const lastNumber = parseInt(lastId.split('-')[1]);
      nextId = lastNumber + 1;
    }
    
    return `GAP-${nextId.toString().padStart(3, '0')}`;
  } catch (error) {
    logger.error('Error generating gap ID:', error);
    throw new Error(`Failed to generate gap ID: ${error.message}`);
  }
};

// Create a new gap
const create = async (gap) => {
  try {
    const pool = await getPool();
    
    // Generate ID if not provided
    if (!gap.GapID) {
      gap.GapID = await generateGapId();
    }
    
    await pool.request()
      .input('GapID', sql.NVarChar(20), gap.GapID)
      .input('GapDescription', sql.NVarChar(sql.MAX), gap.GapDescription)
      .input('GapSeverity', sql.NVarChar(20), gap.GapSeverity)
      .input('GapStatus', sql.NVarChar(20), gap.GapStatus || 'Open')
      .input('RelatedRequirementID', sql.NVarChar(20), gap.RelatedRequirementID)
      .input('GapType', sql.NVarChar(50), gap.GapType)
      .input('ResolutionPlan', sql.NVarChar(sql.MAX), gap.ResolutionPlan)
      .input('AssignedTo', sql.NVarChar(100), gap.AssignedTo)
      .input('DueDate', sql.DateTime, gap.DueDate ? new Date(gap.DueDate) : null)
      .input('CreatedBy', sql.NVarChar(100), gap.CreatedBy)
      .query(`
        INSERT INTO Gaps (
          GapID, GapDescription, GapSeverity, GapStatus, RelatedRequirementID,
          GapType, ResolutionPlan, AssignedTo, DueDate, CreatedBy,
          CreatedDate, LastUpdatedDate
        )
        VALUES (
          @GapID, @GapDescription, @GapSeverity, @GapStatus, @RelatedRequirementID,
          @GapType, @ResolutionPlan, @AssignedTo, @DueDate, @CreatedBy,
          GETDATE(), GETDATE()
        )
      `);
    
    return gap.GapID;
  } catch (error) {
    logger.error('Error creating gap:', error);
    throw new Error(`Failed to create gap: ${error.message}`);
  }
};

// Update an existing gap
const update = async (id, gap) => {
  try {
    const pool = await getPool();
    await pool.request()
      .input('GapID', sql.NVarChar(20), id)
      .input('GapDescription', sql.NVarChar(sql.MAX), gap.GapDescription)
      .input('GapSeverity', sql.NVarChar(20), gap.GapSeverity)
      .input('GapStatus', sql.NVarChar(20), gap.GapStatus)
      .input('RelatedRequirementID', sql.NVarChar(20), gap.RelatedRequirementID)
      .input('GapType', sql.NVarChar(50), gap.GapType)
      .input('ResolutionPlan', sql.NVarChar(sql.MAX), gap.ResolutionPlan)
      .input('AssignedTo', sql.NVarChar(100), gap.AssignedTo)
      .input('DueDate', sql.DateTime, gap.DueDate ? new Date(gap.DueDate) : null)
      .input('UpdatedBy', sql.NVarChar(100), gap.UpdatedBy)
      .query(`
        UPDATE Gaps
        SET GapDescription = @GapDescription,
            GapSeverity = @GapSeverity,
            GapStatus = @GapStatus,
            RelatedRequirementID = @RelatedRequirementID,
            GapType = @GapType,
            ResolutionPlan = @ResolutionPlan,
            AssignedTo = @AssignedTo,
            DueDate = @DueDate,
            UpdatedBy = @UpdatedBy,
            LastUpdatedDate = GETDATE()
        WHERE GapID = @GapID
      `);
    
    return id;
  }
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\requirementModel.js
=============================================================================

Chunk 1/3:
```
const { getPool, sql } = require('../config/database');
const logger = require('../config/logger');

// Generate unique RequirementID
const generateRequirementId = async () => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .query(`
        SELECT TOP 1 RequirementID FROM Requirements
        WHERE RequirementID LIKE 'REQ-%'
        ORDER BY RequirementID DESC
      `);
    
    let nextId = 1;
    if (result.recordset.length > 0) {
      const lastId = result.recordset[0].RequirementID;
      const lastNumber = parseInt(lastId.split('-')[1]);
      nextId = lastNumber + 1;
    }
    
    return `REQ-${nextId.toString().padStart(3, '0')}`;
  } catch (error) {
    logger.error('Error generating requirement ID:', error);
    throw new Error(`Failed to generate requirement ID: ${error.message}`);
  }
};

// Create a new requirement
const create = async (requirement) => {
  try {
    const pool = await getPool();
    
    // Generate ID if not provided
    if (!requirement.RequirementID) {
      requirement.RequirementID = await generateRequirementId();
    }
    
    await pool.request()
      .input('RequirementID', sql.NVarChar(20), requirement.RequirementID)
      .input('RequirementTitle', sql.NVarChar(255), requirement.RequirementTitle)
      .input('RequirementDescription', sql.NVarChar(sql.MAX), requirement.RequirementDescription)
      .input('RequirementType', sql.NVarChar(50), requirement.RequirementType)
      .input('RequirementCategory', sql.NVarChar(50), requirement.RequirementCategory)
      .input('Priority', sql.NVarChar(20), requirement.Priority)
      .input('Status', sql.NVarChar(20), requirement.Status || 'Draft')
      .input('RequirementSource', sql.NVarChar(255), requirement.RequirementSource)
      .input('PrimaryStakeholder', sql.NVarChar(100), requirement.PrimaryStakeholder)
      .input('Complexity', sql.NVarChar(20), requirement.Complexity)
      .input('BusinessValue', sql.NVarChar(20), requirement.BusinessValue)
      .input('AcceptanceCriteria', sql.NVarChar(sql.MAX), requirement.AcceptanceCriteria)
      .input('Dependencies', sql.NVarChar(255), requirement.Dependencies)
      .input('Assumptions', sql.NVarChar(sql.MAX), requirement.Assumptions)
      .input('Constraints', sql.NVarChar(sql.MAX), requirement.Constraints)
      .input('VersionNumber', sql.NVarChar(20), requirement.VersionNumber || '1.0')
      .input('TranscriptID', sql.Int, requirement.TranscriptID)
      .input('CreatedBy', sql.NVarChar(100), requirement.CreatedBy)
      .query(`
        INSERT INTO Requirements (
          RequirementID, RequirementTitle, RequirementDescription, RequirementType,
          RequirementCategory, Priority, Status, RequirementSource, PrimaryStakeholder,
          Complexity, BusinessValue, AcceptanceCriteria, Dependencies, Assumptions,
          Constraints, VersionNumber, TranscriptID, CreatedBy, CreatedDate, LastUpdatedDate
        )
        VALUES (
          @RequirementID, @RequirementTitle, @RequirementDescription, @RequirementType,
          @RequirementCategory, @Priority, @Status, @RequirementSource, @PrimaryStakeholder,
          @Complexity, @BusinessValue, @AcceptanceCriteria, @Dependencies, @Assumptions,
          @Constraints, @VersionNumber, @TranscriptID, @CreatedBy, GETDATE(), GETDATE()
        )
      `);
    
    return requirement.RequirementID;
  } catch (error) {
    logger.error('Error creating requirement:', error);
    throw new Error(`Failed to create requirement: ${error.message}`);
  }
};

// Update an existing requirement
const update = async (id, requirement) => {
  try {
    const pool = await getPool();
    await pool.request()
      .input('RequirementID', sql.NVarChar(20), id)
      .input('RequirementTitle', sql.NVarChar(255), requirement.RequirementTitle)
      .input('RequirementDescription', sql.NVarChar(sql.MAX), requirement.RequirementDescription)
      .input('RequirementType', sql.NVarChar(50), requirement.RequirementT
```


Chunk 2/3:
```
ype)
      .input('RequirementCategory', sql.NVarChar(50), requirement.RequirementCategory)
      .input('Priority', sql.NVarChar(20), requirement.Priority)
      .input('Status', sql.NVarChar(20), requirement.Status)
      .input('RequirementSource', sql.NVarChar(255), requirement.RequirementSource)
      .input('PrimaryStakeholder', sql.NVarChar(100), requirement.PrimaryStakeholder)
      .input('Complexity', sql.NVarChar(20), requirement.Complexity)
      .input('BusinessValue', sql.NVarChar(20), requirement.BusinessValue)
      .input('AcceptanceCriteria', sql.NVarChar(sql.MAX), requirement.AcceptanceCriteria)
      .input('Dependencies', sql.NVarChar(255), requirement.Dependencies)
      .input('Assumptions', sql.NVarChar(sql.MAX), requirement.Assumptions)
      .input('Constraints', sql.NVarChar(sql.MAX), requirement.Constraints)
      .input('VersionNumber', sql.NVarChar(20), requirement.VersionNumber)
      .input('UpdatedBy', sql.NVarChar(100), requirement.UpdatedBy)
      .query(`
        UPDATE Requirements
        SET RequirementTitle = @RequirementTitle,
            RequirementDescription = @RequirementDescription,
            RequirementType = @RequirementType,
            RequirementCategory = @RequirementCategory,
            Priority = @Priority,
            Status = @Status,
            RequirementSource = @RequirementSource,
            PrimaryStakeholder = @PrimaryStakeholder,
            Complexity = @Complexity,
            BusinessValue = @BusinessValue,
            AcceptanceCriteria = @AcceptanceCriteria,
            Dependencies = @Dependencies,
            Assumptions = @Assumptions,
            Constraints = @Constraints,
            VersionNumber = @VersionNumber,
            UpdatedBy = @UpdatedBy,
            LastUpdatedDate = GETDATE()
        WHERE RequirementID = @RequirementID
      `);
    
    return id;
  } catch (error) {
    logger.error('Error updating requirement:', error);
    throw new Error(`Failed to update requirement: ${error.message}`);
  }
};

// Update requirement status
const updateStatus = async (id, status, updatedBy) => {
  try {
    const pool = await getPool();
    await pool.request()
      .input('RequirementID', sql.NVarChar(20), id)
      .input('Status', sql.NVarChar(20), status)
      .input('UpdatedBy', sql.NVarChar(100), updatedBy)
      .query(`
        UPDATE Requirements
        SET Status = @Status,
            UpdatedBy = @UpdatedBy,
            LastUpdatedDate = GETDATE()
        WHERE RequirementID = @RequirementID
      `);
    
    return true;
  } catch (error) {
    logger.error('Error updating requirement status:', error);
    throw new Error(`Failed to update requirement status: ${error.message}`);
  }
};

// Get requirement by ID
const getById = async (id) => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .input('RequirementID', sql.NVarChar(20), id)
      .query(`
        SELECT * FROM Requirements
        WHERE RequirementID = @RequirementID
      `);
    
    return result.recordset[0];
  } catch (error) {
    logger.error('Error fetching requirement by ID:', error);
    throw new Error(`Failed to fetch requirement: ${error.message}`);
  }
};

// Get all requirements with optional filters
const getAll = async (filters = {}) => {
  try {
    const pool = await getPool();
    
    let query = `
      SELECT * FROM Requirements
      WHERE 1=1
    `;
    
    const parameters = {};
    
    // Apply filters if provided
    if (filters.status) {
      query += ' AND Status = @Status';
      parameters.Status = filters.status;
    }
    
    if (filters.priority) {
      query += ' AND Priority = @Priority';
      parameters.Priority = filters.priority;
    }
    
    if (filters.type) {
      query += ' AND RequirementType = @RequirementType';
      parameters.RequirementType = filters.type;
    }
    
    if (filters.search) {
      query += ' AND (RequirementTitle LIKE @Search OR RequirementDescription LIK
```


Chunk 3/3:
```
E @Search)';
      parameters.Search = `%${filters.search}%`;
    }
    
    if (filters.transcriptId) {
      query += ' AND TranscriptID = @TranscriptID';
      parameters.TranscriptID = filters.transcriptId;
    }
    
    // Add sorting
    query += ` ORDER BY ${filters.sortBy || 'LastUpdatedDate'} ${filters.sortDirection || 'DESC'}`;
    
    // Create request with parameters
    const request = pool.request();
    
    // Add all parameters to the request
    Object.entries(parameters).forEach(([key, value]) => {
      request.input(key, value);
    });
    
    const result = await request.query(query);
    return result.recordset;
  } catch (error) {
    logger.error('Error fetching requirements:', error);
    throw new Error(`Failed to fetch requirements: ${error.message}`);
  }
};

// Get requirements by transcript ID
const getByTranscriptId = async (transcriptId) => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .input('TranscriptID', sql.Int, transcriptId)
      .query(`
        SELECT * FROM Requirements
        WHERE TranscriptID = @TranscriptID
      `);
    
    return result.recordset;
  } catch (error) {
    logger.error('Error fetching requirements by transcript ID:', error);
    throw new Error(`Failed to fetch requirements by transcript: ${error.message}`);
  }
};

// Delete requirement
const remove = async (id) => {
  try {
    const pool = await getPool();
    await pool.request()
      .input('RequirementID', sql.NVarChar(20), id)
      .query(`
        DELETE FROM Requirements
        WHERE RequirementID = @RequirementID
      `);
    
    return true;
  } catch (error) {
    logger.error('Error deleting requirement:', error);
    throw new Error(`Failed to delete requirement: ${error.message}`);
  }
};

module.exports = {
  create,
  update,
  updateStatus,
  getById,
  getAll,
  getByTranscriptId,
  remove
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\transcriptModel.js
============================================================================

Chunk 1/1:
```
const { getPool, sql } = require('../config/database');
const logger = require('../config/logger');

// Create a new transcript
const create = async (transcript) => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .input('Title', sql.NVarChar(255), transcript.title)
      .input('Content', sql.NVarChar(sql.MAX), transcript.content)
      .input('MeetingDate', sql.DateTime, new Date(transcript.meetingDate))
      .input('UploadedBy', sql.NVarChar(100), transcript.uploadedBy)
      .input('ProcessingStatus', sql.NVarChar(50), 'Pending')
      .query(`
        INSERT INTO Transcripts (Title, Content, MeetingDate, UploadedBy, ProcessingStatus, UploadedDate)
        VALUES (@Title, @Content, @MeetingDate, @UploadedBy, @ProcessingStatus, GETDATE());
        
        SELECT SCOPE_IDENTITY() AS TranscriptID;
      `);
    
    return result.recordset[0].TranscriptID;
  } catch (error) {
    logger.error('Error creating transcript:', error);
    throw new Error(`Failed to create transcript: ${error.message}`);
  }
};

// Update transcript processing status
const updateStatus = async (id, status, errors = null) => {
  try {
    const pool = await getPool();
    await pool.request()
      .input('TranscriptID', sql.Int, id)
      .input('ProcessingStatus', sql.NVarChar(50), status)
      .input('ProcessingErrors', sql.NVarChar(sql.MAX), errors)
      .query(`
        UPDATE Transcripts
        SET ProcessingStatus = @ProcessingStatus,
            ProcessingErrors = @ProcessingErrors
        WHERE TranscriptID = @TranscriptID
      `);
    
    return true;
  } catch (error) {
    logger.error(`Error updating transcript status to ${status}:`, error);
    throw new Error(`Failed to update transcript status: ${error.message}`);
  }
};

// Get transcript by ID
const getById = async (id) => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .input('TranscriptID', sql.Int, id)
      .query(`
        SELECT * FROM Transcripts
        WHERE TranscriptID = @TranscriptID
      `);
    
    return result.recordset[0];
  } catch (error) {
    logger.error('Error fetching transcript by ID:', error);
    throw new Error(`Failed to fetch transcript: ${error.message}`);
  }
};

// Get all transcripts
const getAll = async () => {
  try {
    const pool = await getPool();
    const result = await pool.request()
      .query(`
        SELECT TranscriptID, Title, MeetingDate, UploadedDate,
               UploadedBy, ProcessingStatus
        FROM Transcripts
        ORDER BY UploadedDate DESC
      `);
    
    return result.recordset;
  } catch (error) {
    logger.error('Error fetching all transcripts:', error);
    throw new Error(`Failed to fetch transcripts: ${error.message}`);
  }
};

// Delete transcript
const remove = async (id) => {
  try {
    const pool = await getPool();
    await pool.request()
      .input('TranscriptID', sql.Int, id)
      .query(`
        DELETE FROM Transcripts
        WHERE TranscriptID = @TranscriptID
      `);
    
    return true;
  } catch (error) {
    logger.error('Error deleting transcript:', error);
    throw new Error(`Failed to delete transcript: ${error.message}`);
  }
};

module.exports = {
  create,
  updateStatus,
  getById,
  getAll,
  remove
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\models\userModel.js
======================================================================

Chunk 1/2:
```
const { getPool, sql } = require('../config/database');
const logger = require('../config/logger');
const { v4: uuidv4 } = require('uuid');

/**
 * User model for handling user-related database operations
 */
class UserModel {
  /**
   * Create a new user
   * @param {Object} userData - User data to create
   * @returns {Promise<string>} - Created user ID
   */
  async create(userData) {
    try {
      const pool = await getPool();
      
      // Generate UUID for user ID
      const userId = uuidv4();
      
      // Insert user into database
      await pool.request()
        .input('UserID', sql.NVarChar(50), userId)
        .input('Email', sql.NVarChar(100), userData.Email)
        .input('PasswordHash', sql.NVarChar(255), userData.PasswordHash)
        .input('FirstName', sql.NVarChar(50), userData.FirstName)
        .input('LastName', sql.NVarChar(50), userData.LastName)
        .input('Role', sql.NVarChar(20), userData.Role || 'User')
        .input('Department', sql.NVarChar(100), userData.Department)
        .input('Avatar', sql.NVarChar(255), userData.Avatar)
        .query(`
          INSERT INTO Users (
            UserID, Email, PasswordHash, FirstName, LastName,
            Role, Department, Avatar, CreatedDate, IsActive
          )
          VALUES (
            @UserID, @Email, @PasswordHash, @FirstName, @LastName,
            @Role, @Department, @Avatar, GETDATE(), 1
          )
        `);
      
      logger.info(`Created new user with ID: ${userId}`);
      return userId;
    } catch (error) {
      logger.error('Error creating user:', error);
      throw new Error(`Failed to create user: ${error.message}`);
    }
  }

  /**
   * Get user by ID
   * @param {string} id - User ID
   * @returns {Promise<Object>} - User data
   */
  async getById(id) {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .input('UserID', sql.NVarChar(50), id)
        .query(`
          SELECT * FROM Users
          WHERE UserID = @UserID
        `);
      
      return result.recordset[0];
    } catch (error) {
      logger.error(`Error fetching user by ID ${id}:`, error);
      throw new Error(`Failed to fetch user: ${error.message}`);
    }
  }

  /**
   * Get user by email
   * @param {string} email - User email
   * @returns {Promise<Object>} - User data
   */
  async getByEmail(email) {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .input('Email', sql.NVarChar(100), email)
        .query(`
          SELECT * FROM Users
          WHERE Email = @Email
        `);
      
      return result.recordset[0];
    } catch (error) {
      logger.error(`Error fetching user by email ${email}:`, error);
      throw new Error(`Failed to fetch user: ${error.message}`);
    }
  }

  /**
   * Get all users
   * @returns {Promise<Array>} - Array of users
   */
  async getAll() {
    try {
      const pool = await getPool();
      const result = await pool.request()
        .query(`
          SELECT UserID, Email, FirstName, LastName, Role, 
                 Department, Avatar, CreatedDate, LastLoginDate, IsActive
          FROM Users
          ORDER BY LastName, FirstName
        `);
      
      return result.recordset;
    } catch (error) {
      logger.error('Error fetching all users:', error);
      throw new Error(`Failed to fetch users: ${error.message}`);
    }
  }

  /**
   * Update user profile
   * @param {string} id - User ID
   * @param {Object} userData - Updated user data
   * @returns {Promise<boolean>} - Success status
   */
  async updateProfile(id, userData) {
    try {
      const pool = await getPool();
      await pool.request()
        .input('UserID', sql.NVarChar(50), id)
        .input('FirstName', sql.NVarChar(50), userData.FirstName)
        .input('LastName', sql.NVarChar(50), userData.LastName)
        .input('Email', sql.NVarChar(100), userData.Email)
        .input('Department', sql.NVarChar(100), userData.Department
```


Chunk 2/2:
```
)
        .input('Avatar', sql.NVarChar(255), userData.Avatar)
        .query(`
          UPDATE Users
          SET FirstName = @FirstName,
              LastName = @LastName,
              Email = @Email,
              Department = @Department,
              Avatar = @Avatar
          WHERE UserID = @UserID
        `);
      
      logger.info(`Updated profile for user ${id}`);
      return true;
    } catch (error) {
      logger.error(`Error updating profile for user ${id}:`, error);
      throw new Error(`Failed to update profile: ${error.message}`);
    }
  }

  /**
   * Update user password
   * @param {string} id - User ID
   * @param {string} passwordHash - New password hash
   * @returns {Promise<boolean>} - Success status
   */
  async updatePassword(id, passwordHash) {
    try {
      const pool = await getPool();
      await pool.request()
        .input('UserID', sql.NVarChar(50), id)
        .input('PasswordHash', sql.NVarChar(255), passwordHash)
        .query(`
          UPDATE Users
          SET PasswordHash = @PasswordHash
          WHERE UserID = @UserID
        `);
      
      logger.info(`Updated password for user ${id}`);
      return true;
    } catch (error) {
      logger.error(`Error updating password for user ${id}:`, error);
      throw new Error(`Failed to update password: ${error.message}`);
    }
  }

  /**
   * Update user last login date
   * @param {string} id - User ID
   * @returns {Promise<boolean>} - Success status
   */
  async updateLastLogin(id) {
    try {
      const pool = await getPool();
      await pool.request()
        .input('UserID', sql
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\auth.routes.js
========================================================================

Chunk 1/1:
```
const express = require('express');
const router = express.Router();
const AuthController = require('../controllers/auth.controller');

// Auth routes
router.post('/login', AuthController.login);
router.post('/register', AuthController.register);
router.post('/logout', AuthController.logout);
router.get('/verify', AuthController.verifyToken);

module.exports = router;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\gaproutes.js
======================================================================

Chunk 1/1:
```
Thoughts

Routes for Transcript-to-Requirements System
Let's create the route files for your backend system:

transcriptRoutes.js
javascript
Run Code
Copy code
const express = require('express');
const router = express.Router();
const transcriptController = require('../controllers/transcriptController');
const { protect } = require('../middleware/authMiddleware');
const { transcriptValidation } = require('../middleware/validation');

// Protect all routes
router.use(protect);

// @route   POST /api/transcripts
// @desc    Upload and process a new transcript
// @access  Private
router.post('/', transcriptValidation.create, transcriptController.uploadTranscript);

// @route   GET /api/transcripts
// @desc    Get all transcripts
// @access  Private
router.get('/', transcriptController.getTranscripts);

// @route   GET /api/transcripts/:id
// @desc    Get single transcript by ID
// @access  Private
router.get('/:id', transcriptController.getTranscriptById);

// @route   GET /api/transcripts/:id/requirements
// @desc    Get requirements generated from a transcript
// @access  Private
router.get('/:id/requirements', transcriptController.getTranscriptRequirements);

// @route   DELETE /api/transcripts/:id
// @desc    Delete a transcript
// @access  Private
router.delete('/:id', transcriptController.deleteTranscript);

module.exports = router;
requirementRoutes.js
javascript
Run Code
Copy code
const express = require('express');
const router = express.Router();
const requirementController = require('../controllers/requirementController');
const { protect } = require('../middleware/authMiddleware');
const { requirementValidation } = require('../middleware/validation');

// Protect all routes
router.use(protect);

// @route   GET /api/requirements
// @desc    Get all requirements with optional filtering
// @access  Private
router.get('/', requirementController.getRequirements);

// @route   GET /api/requirements/:id
// @desc    Get single requirement by ID
// @access  Private
router.get('/:id', requirementController.getRequirementById);

// @route   POST /api/requirements
// @desc    Create a new requirement
// @access  Private
router.post('/', requirementValidation.create, requirementController.createRequirement);

// @route   PUT /api/requirements/:id
// @desc    Update a requirement
// @access  Private
router.put('/:id', requirementValidation.update, requirementController.updateRequirement);

// @route   PATCH /api/requirements/:id/status
// @desc    Update requirement status
// @access  Private
router.patch('/:id/status', requirementValidation.updateStatus, requirementController.updateRequirementStatus);

// @route   DELETE /api/requirements/:id
// @desc    Delete a requirement
// @access  Private
router.delete('/:id', requirementController.deleteRequirement);

// @route   GET /api/requirements/:id/gaps
// @desc    Get gaps associated with a requirement
// @access  Private
router.get('/:id/gaps', requirementController.getRequirementGaps);

module.exports = router;
gapRoutes.js
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\requirementRoutes.js
==============================================================================

Chunk 1/1:
```
const express = require('express');
const router = express.Router();
const requirementController = require('../controllers/requirementController');
const { protect } = require('../middleware/authMiddleware');
const { requirementValidation } = require('../middleware/validation');

// Protect all routes
router.use(protect);

// @route   GET /api/requirements
// @desc    Get all requirements with optional filtering
// @access  Private
router.get('/', requirementController.getRequirements);

// @route   GET /api/requirements/:id
// @desc    Get single requirement by ID
// @access  Private
router.get('/:id', requirementController.getRequirementById);

// @route   POST /api/requirements
// @desc    Create a new requirement
// @access  Private
router.post('/', requirementValidation.create, requirementController.createRequirement);

// @route   PUT /api/requirements/:id
// @desc    Update a requirement
// @access  Private
router.put('/:id', requirementValidation.update, requirementController.updateRequirement);

// @route   PATCH /api/requirements/:id/status
// @desc    Update requirement status
// @access  Private
router.patch('/:id/status', requirementValidation.updateStatus, requirementController.updateRequirementStatus);

// @route   DELETE /api/requirements/:id
// @desc    Delete a requirement
// @access  Private
router.delete('/:id', requirementController.deleteRequirement);

// @route   GET /api/requirements/:id/gaps
// @desc    Get gaps associated with a requirement
// @access  Private
router.get('/:id/gaps', requirementController.getRequirementGaps);

module.exports = router;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\stakeholderRoutes.js
==============================================================================

Chunk 1/1:
```
const express = require('express');
const router = express.Router();
const stakeholderController = require('../controllers/stakeholderController');
const { protect } = require('../middleware/authMiddleware');
const { stakeholderValidation } = require('../middleware/validation');

// Protect all routes
router.use(protect);

// @route   GET /api/stakeholders
// @desc    Get all stakeholders with optional filtering
// @access  Private
router.get('/', stakeholderController.getStakeholders);

// @route   GET /api/stakeholders/:id
// @desc    Get single stakeholder by ID
// @access  Private
router.get('/:id', stakeholderController.getStakeholderById);

// @route   POST /api/stakeholders
// @desc    Create a new stakeholder
// @access  Private
router.post('/', stakeholderValidation.create, stakeholderController.createStakeholder);

// @route   PUT /api/stakeholders/:id
// @desc    Update a stakeholder
// @access  Private
router.put('/:id', stakeholderValidation.update, stakeholderController.updateStakeholder);

// @route   DELETE /api/stakeholders/:id
// @desc    Delete a stakeholder
// @access  Private
router.delete('/:id', stakeholderController.deleteStakeholder);

// @route   GET /api/stakeholders/:id/requirements
// @desc    Get requirements associated with a stakeholder
// @access  Private
router.get('/:id/requirements', stakeholderController.getStakeholderRequirements);

module.exports = router;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\transcriptRoutes.js
=============================================================================

Chunk 1/1:
```
const express = require('express');
const router = express.Router();
const transcriptController = require('../controllers/transcriptController');
const { protect } = require('../middleware/authMiddleware');
const { transcriptValidation } = require('../middleware/validation');

// Protect all routes
router.use(protect);

// @route   POST /api/transcripts
// @desc    Upload and process a new transcript
// @access  Private
router.post('/', transcriptValidation.create, transcriptController.uploadTranscript);

// @route   GET /api/transcripts
// @desc    Get all transcripts
// @access  Private
router.get('/', transcriptController.getTranscripts);

// @route   GET /api/transcripts/:id
// @desc    Get single transcript by ID
// @access  Private
router.get('/:id', transcriptController.getTranscriptById);

// @route   GET /api/transcripts/:id/requirements
// @desc    Get requirements generated from a transcript
// @access  Private
router.get('/:id/requirements', transcriptController.getTranscriptRequirements);

// @route   DELETE /api/transcripts/:id
// @desc    Delete a transcript
// @access  Private
router.delete('/:id', transcriptController.deleteTranscript);

module.exports = router;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\routes\userRoutes.js
=======================================================================

Chunk 1/1:
```
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const { protect, authorize } = require('../middleware/authMiddleware');
const { userValidation } = require('../middleware/validation');

// Public routes
// @route   POST /api/users/register
// @desc    Register a new user
// @access  Public
router.post('/register', userValidation.register, userController.registerUser);

// @route   POST /api/users/login
// @desc    Authenticate a user and get token
// @access  Public
router.post('/login', userValidation.login, userController.loginUser);

// Protected routes
router.use(protect);

// @route   GET /api/users/me
// @desc    Get current user profile
// @access  Private
router.get('/me', userController.getMe);

// @route   PUT /api/users/me
// @desc    Update user profile
// @access  Private
router.put('/me', userValidation.updateProfile, userController.updateProfile);

// Admin-only routes
// @route   GET /api/users
// @desc    Get all users
// @access  Private/Admin
router.get('/', authorize('Admin'), userController.getUsers);

module.exports = router;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\geminiService.js
============================================================================

Chunk 1/3:
```
const { getModel } = require('../config/gemini');
const logger = require('../config/logger');

/**
 * Service for interaction with Google's Gemini AI models
 */
class GeminiService {
  /**
   * Analyze a meeting transcript to extract structured requirements, gaps, and stakeholders
   * @param {string} transcript - The meeting transcript text
   * @returns {Promise<Object>} - Structured data containing requirements, gaps, and stakeholders
   */
  async analyzeTranscript(transcript) {
    try {
      logger.info('Starting transcript analysis with Gemini AI');
      const model = getModel();
      
      // Construct prompt for requirement extraction
      const prompt = this._constructRequirementsPrompt(transcript);
      
      // Call Gemini API
      logger.debug('Sending request to Gemini API');
      const result = await model.generateContent(prompt);
      const response = await result.response;
      const text = response.text();
      
      logger.info('Received response from Gemini API');
      
      // Parse and validate the response
      return this._parseGeminiResponse(text);
    } catch (error) {
      logger.error('Error in Gemini transcript analysis:', error);
      throw new Error(`Gemini analysis failed: ${error.message}`);
    }
  }

  /**
   * Construct a detailed prompt for Gemini to extract requirements
   * @param {string} transcript - The meeting transcript
   * @returns {string} - The formatted prompt
   * @private
   */
  _constructRequirementsPrompt(transcript) {
    return `
      You are a requirements analyst tasked with extracting structured information from a meeting transcript.
      
      Analyze the following meeting transcript and extract:
      1. Requirements (with IDs starting with REQ-)
      2. Gaps (with IDs starting with GAP-)
      3. Stakeholders (with IDs starting with SH-)
      
      For each requirement, identify:
      - RequirementTitle: A short descriptive title (maximum 10 words)
      - RequirementDescription: Detailed explanation using "shall" statements
      - RequirementType: Functional or Non-Functional
      - RequirementCategory: User Interface, Security, Performance, Data, Integration, etc.
      - Priority: High, Medium, or Low
      - Status: Draft
      - PrimaryStakeholder: The main person who needs this requirement
      - Complexity: Simple, Moderate, or Complex
      - BusinessValue: High, Medium, or Low
      - AcceptanceCriteria: How we can verify this requirement is met
      
      For each gap, identify:
      - GapDescription: Detailed explanation of missing information
      - GapSeverity: Critical, Major, or Minor
      - GapStatus: Open
      - RelatedRequirementID: Which requirement this gap relates to (use the REQ-XXX ID)
      - GapType: Missing Information, Conflict, Ambiguity, or Technical Feasibility
      
      For each stakeholder, identify:
      - StakeholderName: Person's name
      - StakeholderRole: Their role in the project
      - ContactInformation: If available
      - InfluenceLevel: Decision Maker, Influencer, or Informed
      - InterestLevel: High, Medium, or Low
      
      Format your response as a valid JSON with these sections: requirements, gaps, stakeholders.
      Don't include explanations outside the JSON. The JSON should be parseable by JavaScript JSON.parse().
      
      Meeting Transcript:
      ${transcript}
    `;
  }

  /**
   * Parse and validate the response from Gemini
   * @param {string} responseText - The raw response text
   * @returns {Object} - Parsed and validated response
   * @private
   */
  _parseGeminiResponse(responseText) {
    try {
      // Attempt to extract JSON from the response
      let jsonMatch = responseText.match(/```json\n([\s\S]*?)\n```/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[1]);
      }
      
      // Try extracting JSON without code blocks
      jsonMatch = responseText.match(/{[\s\S]*}/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[0]);
 
```


Chunk 2/3:
```
     }
      
      // If no JSON found, try parsing the entire text
      return JSON.parse(responseText);
    } catch (error) {
      logger.error('Error parsing Gemini response:', error);
      logger.debug('Raw response text:', responseText);
      throw new Error('Failed to parse structured data from Gemini response');
    }
  }

  /**
   * Generate a concise description for a requirement
   * @param {Object} requirement - The requirement object
   * @returns {Promise<string>} - AI-generated description
   */
  async generateRequirementDescription(requirement) {
    try {
      const model = getModel();
      
      const prompt = `
        You are a technical writer specializing in software requirements.
        
        Create a clear, concise requirement description in the format "The system shall..."
        
        Requirement Context:
        - Title: ${requirement.RequirementTitle}
        - Type: ${requirement.RequirementType || 'Not specified'}
        - Category: ${requirement.RequirementCategory || 'Not specified'}
        - Priority: ${requirement.Priority || 'Not specified'}
        
        ${requirement.RequirementDescription ? 'Current description: ' + requirement.RequirementDescription : ''}
        
        Write a well-structured requirement description that is specific, measurable, achievable, relevant, and time-bound (SMART).
        Limit your response to 2-3 sentences, focusing only on the requirement description.
      `;
      
      const result = await model.generateContent(prompt);
      return result.response.text().trim();
    } catch (error) {
      logger.error('Error generating requirement description:', error);
      throw new Error(`Failed to generate requirement description: ${error.message}`);
    }
  }

  /**
   * Generate acceptance criteria for a requirement
   * @param {Object} requirement - The requirement object
   * @returns {Promise<string>} - AI-generated acceptance criteria
   */
  async generateAcceptanceCriteria(requirement) {
    try {
      const model = getModel();
      
      const prompt = `
        You are a quality assurance expert specializing in software requirements.
        
        Create clear acceptance criteria for the following requirement:
        
        Requirement: ${requirement.RequirementTitle}
        Description: ${requirement.RequirementDescription}
        Type: ${requirement.RequirementType || 'Not specified'}
        
        Generate 3-5 specific, testable acceptance criteria that would verify this requirement has been met.
        Format each criterion as a bullet point starting with "- " and ensure they are measurable.
        Limit your response to only the bullet-pointed list of acceptance criteria.
      `;
      
      const result = await model.generateContent(prompt);
      return result.response.text().trim();
    } catch (error) {
      logger.error('Error generating acceptance criteria:', error);
      throw new Error(`Failed to generate acceptance criteria: ${error.message}`);
    }
  }

  /**
   * Suggest gap resolutions for identified gaps
   * @param {Object} gap - The gap object
   * @returns {Promise<string>} - AI-generated resolution suggestions
   */
  async suggestGapResolution(gap) {
    try {
      const model = getModel();
      
      const prompt = `
        You are a requirements analyst specializing in resolving information gaps.
        
        Suggest a resolution plan for the following gap:
        
        Gap Description: ${gap.GapDescription}
        Gap Type: ${gap.GapType || 'Not specified'}
        Gap Severity: ${gap.GapSeverity || 'Not specified'}
        Related Requirement: ${gap.RelatedRequirementID || 'Not specified'}
        
        Provide specific steps to resolve this gap, including:
        1. What information needs to be gathered
        2. From whom it should be gathered
        3. Methods to gather the information (e.g., interview, survey, workshop)
        4. Timeline recommendation
       
```


Chunk 3/3:
```
 
        Limit your response to 3-5 specific, actionable recommendations.
      `;
      
      const result = await model.generateContent(prompt);
      return result.response.text().trim();
    } catch (error) {
      logger.error('Error suggesting gap resolution:', error);
      throw new Error(`Failed to suggest gap resolution: ${error.message}`);
    }
  }

  /**
   * Analyze requirements to identify potential missing requirements
   * @param {Array} requirements - List of current requirements
   * @returns {Promise<Array>} - List of potentially missing requirements
   */
  async identifyMissingRequirements(requirements) {
    try {
      const model = getModel();
      
      // Extract essential information from requirements to reduce token usage
      const simplifiedRequirements = requirements.map(req => ({
        id: req.RequirementID,
        title: req.RequirementTitle,
        description: req.RequirementDescription,
        type: req.RequirementType,
        category: req.RequirementCategory
      }));
      
      const prompt = `
        You are a requirements completeness analyst.
        
        Review these existing requirements:
        ${JSON.stringify(simplifiedRequirements, null, 2)}
        
        Identify potential missing requirements that should be considered based on the existing set.
        Consider common requirement categories such as:
        - Security requirements
        - Performance requirements
        - Usability requirements
        - Compliance requirements
        - Error handling requirements
        - Backup and recovery requirements
        
        For each missing requirement you identify, provide:
        - A suggested title
        - A brief description
        - The requirement type
        - The requirement category
        - Justification for why it should be included
        
        Return your response as a JSON array of missing requirements, with each having the properties: title, description, type, category, and justification.
        Limit your response to the JSON array only.
      `;
      
      const result = await model.generateContent(prompt);
      const text = result.response.text();
      
      // Parse the response
      try {
        const jsonMatch = text.match(/\[\s*\{[\s\S]*\}\s*\]/);
        if (jsonMatch) {
          return JSON.parse(jsonMatch[0]);
        }
        return [];
      } catch (error) {
        logger.error('Error parsing missing requirements response:', error);
        return [];
      }
    } catch (error) {
      logger.error('Error identifying missing requirements:', error);
      throw new Error(`Failed to identify missing requirements: ${error.message}`);
    }
  }
}

module.exports = new GeminiService();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\nlpService.js
=========================================================================

Chunk 1/1:
```
const natural = require('natural');
const tokenizer = new natural.WordTokenizer();
const stopwords = require('stopwords').english;

// Simplified NLP service
async function processText(text) {
  try {
    // Tokenize and remove stopwords
    const tokens = tokenizer.tokenize(text)
      .map(token => token.toLowerCase())
      .filter(token => !stopwords.includes(token));
    
    // Extract keywords (most frequent words)
    const frequencies = {};
    tokens.forEach(token => {
      frequencies[token] = (frequencies[token] || 0) + 1;
    });
    
    const keywords = Object.entries(frequencies)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(entry => entry[0]);
    
    // Generate summary (first 100 characters)
    const summary = text.length > 100 ? text.substring(0, 97) + '...' : text;
    
    // Determine category based on keywords
    const categoryMapping = {
      'security': 'Security',
      'login': 'Authentication',
      'user': 'User Management',
      'interface': 'UI/UX',
      'data': 'Data Management',
      'api': 'Integration',
      'mobile': 'Mobile',
      'performance': 'Performance',
      'test': 'Quality Assurance'
    };
    
    let category = 'General';
    for (const [keyword, mappedCategory] of Object.entries(categoryMapping)) {
      if (text.toLowerCase().includes(keyword)) {
        category = mappedCategory;
        break;
      }
    }
    
    // Determine urgency based on keywords
    let urgency = 'Medium';
    if (text.toLowerCase().includes('urgent') || text.toLowerCase().includes('immediately')) {
      urgency = 'High';
    } else if (text.toLowerCase().includes('when possible') || text.toLowerCase().includes('low priority')) {
      urgency = 'Low';
    }
    
    // Extract due date (simplified approach)
    let dueDate = null;
    if (text.toLowerCase().includes('due') || text.toLowerCase().includes('by')) {
      // This is very simplified - in a real app you'd want to use a date parsing library
      const datePattern = /(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{4})/;
      const match = text.match(datePattern);
      if (match) {
        dueDate = new Date(`${match[3]}-${match[2]}-${match[1]}`);
      }
    }
    
    return {
      keywords: keywords.join(', '),
      summary,
      category,
      urgency,
      dueDate,
      confidenceScore: calculateConfidence(text, keywords)
    };
  } catch (error) {
    console.error('Error in NLP processing:', error);
    throw error;
  }
}

function calculateConfidence(text, keywords) {
  // Simple confidence calculation
  const wordCount = text.split(' ').length;
  return Math.min(100, Math.max(50, 60 + keywords.length * 5 + Math.min(20, wordCount / 10)));
}

module.exports = { processText };
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\requirementService.js
=================================================================================

Chunk 1/1:
```
const Requirement = require('../models/requirement');
const { processText } = require('./geminiService'); // Change from nlpService to geminiService
const { generateRequirementId } = require('../utils/idGenerator');

async function createRequirementFromSpeech(transcription, username) {
  try {
    // Process the transcription with NLP
    const processed = await processText(transcription);
    
    // Create a name from the first few words
    const words = transcription.split(' ');
    const name = words.length > 5 
      ? words.slice(0, 5).join(' ') + '...'
      : transcription;
    
    // Create the requirement object
    const requirement = {
      requirementId: generateRequirementId(),
      name,
      description: transcription,
      summary: processed.summary,
      keywords: processed.keywords,
      category: processed.category,
      urgency: processed.urgency,
      dueDate: processed.dueDate,
      createdUser: username,
      teamToProcess: determineTeam(processed.category),
      status: 'New',
      confidenceScore: processed.confidenceScore
    };
    
    // Save to database
    const savedRequirement = await Requirement.create(requirement);
    return savedRequirement;
  } catch (error) {
    console.error('Error creating requirement:', error);
    throw error;
  }
}

function determineTeam(category) {
  // Map categories to teams
  const teamMapping = {
    'Security': 'Security Team',
    'Authentication': 'Authentication Team',
    'User Management': 'User Management Team',
    'UI/UX': 'UI/UX Team',
    'Data Management': 'Data Team',
    'Integration': 'API Team',
    'Mobile': 'Mobile Team',
    'Performance': 'Performance Team',
    'Quality Assurance': 'QA Team'
  };
  
  return teamMapping[category] || 'General Development Team';
}

async function updateRequirement(id, updates) {
  try {
    const requirement = await Requirement.findByPk(id);
    if (!requirement) {
      throw new Error('Requirement not found');
    }
    
    await requirement.update(updates);
    return requirement;
  } catch (error) {
    console.error('Error updating requirement:', error);
    throw error;
  }
}

async function getAllRequirements() {
  return await Requirement.findAll({
    order: [['createAt', 'DESC']]
  });
}

async function getRequirementById(id) {
  return await Requirement.findByPk(id);
}

module.exports = {
  createRequirementFromSpeech,
  updateRequirement,
  getAllRequirements,
  getRequirementById
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\services\speechService.js
============================================================================

Chunk 1/1:
```
// Using Google Speech-to-Text API
const speech = require('@google-cloud/speech');
const fs = require('fs');

const client = new speech.SpeechClient({
  keyFilename: 'path-to-google-credentials.json'
});

async function transcribeSpeech(audioBuffer) {
  try {
    const audio = {
      content: audioBuffer.toString('base64')
    };
    
    const config = {
      encoding: 'LINEAR16',
      sampleRateHertz: 16000,
      languageCode: 'en-US',
    };
    
    const request = {
      audio: audio,
      config: config,
    };

    const [response] = await client.recognize(request);
    return response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
  } catch (error) {
    console.error('Error in speech transcription:', error);
    throw error;
  }
}

module.exports = { transcribeSpeech };
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\utils\asyncHandler.js
========================================================================

Chunk 1/1:
```
/**
 * Async handler to eliminate try/catch blocks in route handlers
 * @param {Function} fn - Async function to handle the route
 * @returns {Function} - Express middleware function
 */
const asyncHandler = (fn) => {
    return (req, res, next) => {
      Promise.resolve(fn(req, res, next)).catch(next);
    };
  };
  
  module.exports = asyncHandler;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\utils\databaseUtils.js
=========================================================================

Chunk 1/2:
```
const { getPool, sql } = require('../../config/database');
const logger = require('../../config/logger');

/**
 * Database utility functions to simplify common operations
 */
const databaseUtils = {
  /**
   * Executes a SQL query with parameters and returns the results
   * @param {string} query - SQL query to execute
   * @param {Object} params - Query parameters
   * @returns {Promise<Array>} - Query results
   */
  async executeQuery(query, params = {}) {
    try {
      const pool = await getPool();
      const request = pool.request();
      
      // Add parameters to the request
      Object.keys(params).forEach(key => {
        const value = params[key];
        
        // Determine SQL type based on JavaScript value
        if (value === null) {
          request.input(key, sql.NVarChar, null);
        } else if (typeof value === 'number') {
          if (Number.isInteger(value)) {
            request.input(key, sql.Int, value);
          } else {
            request.input(key, sql.Float, value);
          }
        } else if (value instanceof Date) {
          request.input(key, sql.DateTime, value);
        } else if (typeof value === 'boolean') {
          request.input(key, sql.Bit, value);
        } else {
          request.input(key, sql.NVarChar, value);
        }
      });
      
      const result = await request.query(query);
      return result.recordset;
    } catch (error) {
      logger.error('Error executing query:', error);
      throw new Error(`Database query error: ${error.message}`);
    }
  },
  
  /**
   * Generates a unique ID with a prefix and padding
   * @param {string} prefix - ID prefix (e.g., 'REQ-', 'GAP-')
   * @param {string} tableName - Table to check for existing IDs
   * @param {string} idColumn - Column name containing the ID
   * @returns {Promise<string>} - Generated unique ID
   */
  async generateUniqueId(prefix, tableName, idColumn) {
    try {
      const query = `
        SELECT TOP 1 ${idColumn} FROM ${tableName}
        WHERE ${idColumn} LIKE '${prefix}%'
        ORDER BY ${idColumn} DESC
      `;
      
      const results = await this.executeQuery(query);
      
      let nextId = 1;
      if (results.length > 0) {
        const lastId = results[0][idColumn];
        const lastNumber = parseInt(lastId.split('-')[1]);
        nextId = lastNumber + 1;
      }
      
      return `${prefix}${nextId.toString().padStart(3, '0')}`;
    } catch (error) {
      logger.error(`Error generating unique ID with prefix ${prefix}:`, error);
      throw new Error(`Failed to generate unique ID: ${error.message}`);
    }
  },
  
  /**
   * Begins a transaction
   * @returns {Promise<Transaction>} - SQL transaction object
   */
  async beginTransaction() {
    try {
      const pool = await getPool();
      const transaction = new sql.Transaction(pool);
      await transaction.begin();
      return transaction;
    } catch (error) {
      logger.error('Error beginning transaction:', error);
      throw new Error(`Failed to begin transaction: ${error.message}`);
    }
  },
  
  /**
   * Creates a request with the given transaction
   * @param {Transaction} transaction - SQL transaction
   * @returns {Request} - SQL request
   */
  createRequest(transaction) {
    return new sql.Request(transaction);
  },
  
  /**
   * Commits a transaction
   * @param {Transaction} transaction - SQL transaction to commit
   * @returns {Promise<void>}
   */
  async commitTransaction(transaction) {
    try {
      await transaction.commit();
    } catch (error) {
      logger.error('Error committing transaction:', error);
      throw new Error(`Failed to commit transaction: ${error.message}`);
    }
  },
  
  /**
   * Rolls back a transaction
   * @param {Transaction} transaction - SQL transaction to roll back
   * @returns {Promise<void>}
   */
  async rollbackTransaction(transaction) {
    try {
      await transaction.rollback();
    } catch (error) {
      logger.error('Error rolling back transaction:', 
```


Chunk 2/2:
```
error);
    }
  }
};

module.exports = databaseUtils;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\backend\src\utils\idGenerator.js
=======================================================================

Chunk 1/1:
```
function generateRequirementId() {
    const date = new Date();
    const year = date.getFullYear();
    const randomPart = Math.floor(Math.random() * 10000).toString().padStart(4, '0');
    return `REQ-${year}-${randomPart}`;
  }
  
  module.exports = { generateRequirementId };
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\.eslintrc.js
============================================================

Chunk 1/1:
```
module.exports = {
    root: true,
    env: {
      node: true,
      'vue/setup-compiler-macros': true
    },
    extends: [
      'plugin:vue/vue3-essential',
      'eslint:recommended'
    ],
    parserOptions: {
      parser: '@babel/eslint-parser',
      requireConfigFile: false
    },
    rules: {
      'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'vue/multi-word-component-names': 'off',
      'no-unused-vars': ['error', {
        'argsIgnorePattern': '^_',
        'varsIgnorePattern': '^_'
      }],
      'vue/valid-v-slot': ['error', {
        allowModifiers: true
      }]
    }
  };
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\vue.config.js
=============================================================

Chunk 1/1:
```
const path = require('path');

module.exports = {
  transpileDependencies: true,

  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src/')
      }
    }
  },
  chainWebpack: config => {
    config.resolve.alias.set('@', path.resolve(__dirname, 'src'));
  },
  
  devServer: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },

  css: {
    loaderOptions: {
      sass: {
        additionalData: `
          @import "@/assets/styles/variables.scss";
          @import "@/assets/styles/mixins.scss";
        `
      }
    }
  }
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\main.js
===========================================================

Chunk 1/1:
```
/* eslint-disable */
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(vuetify);

app.mount('#app');
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\plugins\vuetify.js
======================================================================

Chunk 1/1:
```
/* eslint-disable */
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { aliases, mdi } from 'vuetify/iconsets/mdi';
import '@mdi/font/css/materialdesignicons.css';

export default createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi
    }
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#1976D2',
          secondary: '#424242',
          accent: '#82B1FF',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107'
        }
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\router\index.js
===================================================================

Chunk 1/1:
```
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/modules/auth'

// Views
import DashboardView from '@/views/DashboardView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import RequirementsView from '@/views/RequirementsView.vue'
import RequirementCreateView from '@/views/RequirementCreateView.vue'
import RequirementEditView from '@/views/RequirementEditView.vue'
import TranscriptsView from '@/views/TranscriptsView.vue'
import TranscriptUploadView from '@/views/TranscriptUploadView.vue'
import GapsView from '@/views/GapsView.vue'
import StakeholdersView from '@/views/StakeholdersView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true, title: 'Dashboard' }
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
    meta: { title: 'Login' }
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
    meta: { title: 'Register' }
  },
  {
    path: '/requirements',
    name: 'Requirements',
    component: RequirementsView,
    meta: { requiresAuth: true, title: 'Requirements' }
  },
  {
    path: '/requirements/create',
    name: 'RequirementCreate',
    component: RequirementCreateView,
    meta: { requiresAuth: true, title: 'Create Requirement' }
  },
  {
    path: '/requirements/:id',
    name: 'RequirementEdit',
    component: RequirementEditView,
    meta: { requiresAuth: true, title: 'Edit Requirement' }
  },
  {
    path: '/transcripts',
    name: 'Transcripts',
    component: TranscriptsView,
    meta: { requiresAuth: true, title: 'Transcripts' }
  },
  {
    path: '/transcripts/upload',
    name: 'TranscriptUpload',
    component: TranscriptUploadView,
    meta: { requiresAuth: true, title: 'Upload Transcript' }
  },
  {
    path: '/gaps',
    name: 'Gaps',
    component: GapsView,
    meta: { requiresAuth: true, title: 'Gaps' }
  },
  {
    path: '/stakeholders',
    name: 'Stakeholders',
    component: StakeholdersView,
    meta: { requiresAuth: true, title: 'Stakeholders' }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true, title: 'Profile' }
  },
  { 
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFoundView,
    meta: { title: 'Page Not Found' }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Navigation guard
router.beforeEach((to, from, next) => {
  // Update document title
  document.title = `${to.meta.title} | ${process.env.VUE_APP_TITLE || 'Requirements Management'}`;
  
  // Check for authenticated routes
  const authStore = useAuthStore();
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  
  if (requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login', query: { redirect: to.fullPath } });
  } else {
    next();
  }
})

export default router
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\api.js
===================================================================

Chunk 1/1:
```
import axios from 'axios';
import router from '@/router';
import { useAuthStore } from '@/store/modules/auth';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:3000/api',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Handle token expiration
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const authStore = useAuthStore();

      try {
        await authStore.refreshToken();
        return api(originalRequest);
      } catch (refreshError) {
        authStore.clearAuthData();
        router.push('/login');
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\authService.js
===========================================================================

Chunk 1/1:
```
import api from './api';

class AuthService {
  async login(credentials) {
    const response = await api.post('/auth/login', credentials);
    return response.data;
  }

  async register(userData) {
    const response = await api.post('/auth/register', userData);
    return response.data;
  }

  async verifyTwoFactor(data) {
    const response = await api.post('/auth/verify-2fa', data);
    return response.data;
  }

  async refreshToken() {
    const response = await api.post('/auth/refresh');
    return response.data;
  }

  async logout() {
    const response = await api.post('/auth/logout');
    return response.data;
  }

  async forgotPassword(email) {
    const response = await api.post('/auth/forgot-password', { email });
    return response.data;
  }

  async resetPassword(token, password) {
    const response = await api.post('/auth/reset-password', { token, password });
    return response.data;
  }

  async changePassword(passwordData) {
    const response = await api.post('/auth/change-password', passwordData);
    return response.data;
  }

  async updateProfile(profileData) {
    const response = await api.put('/auth/profile', profileData);
    return response.data;
  }
}

export default new AuthService();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\gapService.js
==========================================================================

Chunk 1/1:
```
import api from './api';

class GapService {
  async getAllGaps() {
    const response = await api.get('/gaps');
    return response.data;
  }

  async getGapById(id) {
    const response = await api.get(`/gaps/${id}`);
    return response.data;
  }

  async createGap(data) {
    const response = await api.post('/gaps', data);
    return response.data;
  }

  async updateGap(id, data) {
    const response = await api.put(`/gaps/${id}`, data);
    return response.data;
  }

  async deleteGap(id) {
    const response = await api.delete(`/gaps/${id}`);
    return response.data;
  }

  async getGapsByRequirement(requirementId) {
    const response = await api.get(`/gaps/requirement/${requirementId}`);
    return response.data;
  }

  async resolveGap(id, resolution) {
    const response = await api.post(`/gaps/${id}/resolve`, resolution);
    return response.data;
  }

  async assignGap(id, assigneeId) {
    const response = await api.post(`/gaps/${id}/assign`, { assigneeId });
    return response.data;
  }

  async addGapComment(id, comment) {
    const response = await api.post(`/gaps/${id}/comments`, comment);
    return response.data;
  }

  async getGapAnalytics() {
    const response = await api.get('/gaps/analytics');
    return response.data;
  }
}

export default new GapService();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\requirementsService.js
===================================================================================

Chunk 1/1:
```
import api from './api';

class RequirementService {
  async getAllRequirements() {
    const response = await api.get('/requirements');
    return response.data;
  }

  async getRequirementById(id) {
    const response = await api.get(`/requirements/${id}`);
    return response.data;
  }

  async createRequirement(data) {
    const response = await api.post('/requirements', data);
    return response.data;
  }

  async updateRequirement(id, data) {
    const response = await api.put(`/requirements/${id}`, data);
    return response.data;
  }

  async deleteRequirement(id) {
    const response = await api.delete(`/requirements/${id}`);
    return response.data;
  }

  async importRequirements(file) {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post('/requirements/import', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;
  }

  async exportRequirements(format = 'xlsx') {
    const response = await api.get(`/requirements/export?format=${format}`, {
      responseType: 'blob'
    });
    return response.data;
  }

  async validateRequirement(id) {
    const response = await api.post(`/requirements/${id}/validate`);
    return response.data;
  }

  async getRequirementHistory(id) {
    const response = await api.get(`/requirements/${id}/history`);
    return response.data;
  }

  async addRequirementComment(id, comment) {
    const response = await api.post(`/requirements/${id}/comments`, comment);
    return response.data;
  }
}

export default new RequirementService();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\stakeholderService.js
==================================================================================

Chunk 1/1:
```
import api from './api';

class StakeholderService {
  async getAllStakeholders() {
    const response = await api.get('/stakeholders');
    return response.data;
  }

  async getStakeholderById(id) {
    const response = await api.get(`/stakeholders/${id}`);
    return response.data;
  }

  async createStakeholder(data) {
    const response = await api.post('/stakeholders', data);
    return response.data;
  }

  async updateStakeholder(id, data) {
    const response = await api.put(`/stakeholders/${id}`, data);
    return response.data;
  }

  async deleteStakeholder(id) {
    const response = await api.delete(`/stakeholders/${id}`);
    return response.data;
  }

  async importStakeholders(file) {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post('/stakeholders/import', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;
  }

  async exportStakeholders(format = 'xlsx') {
    const response = await api.get(`/stakeholders/export?format=${format}`, {
      responseType: 'blob'
    });
    return response.data;
  }

  async getStakeholderRequirements(id) {
    const response = await api.get(`/stakeholders/${id}/requirements`);
    return response.data;
  }

  async getStakeholderAnalytics(id) {
    const response = await api.get(`/stakeholders/${id}/analytics`);
    return response.data;
  }

  async updateStakeholderInfluence(id, influenceData) {
    const response = await api.put(`/stakeholders/${id}/influence`, influenceData);
    return response.data;
  }

  async getStakeholderMatrix() {
    const response = await api.get('/stakeholders/matrix');
    return response.data;
  }
}

export default new StakeholderService();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\services\transcriptsService.js
==================================================================================

Chunk 1/1:
```
import api from './api';

class TranscriptService {
  async getAllTranscripts() {
    const response = await api.get('/transcripts');
    return response.data;
  }

  async getTranscriptById(id) {
    const response = await api.get(`/transcripts/${id}`);
    return response.data;
  }

  async createTranscript(data) {
    const formData = new FormData();
    
    // Handle file upload if present
    if (data.file) {
      formData.append('file', data.file);
    }
    
    // Append other transcript data
    Object.keys(data).forEach(key => {
      if (key !== 'file') {
        formData.append(key, data[key]);
      }
    });

    const response = await api.post('/transcripts', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;
  }

  async updateTranscript(id, data) {
    const response = await api.put(`/transcripts/${id}`, data);
    return response.data;
  }

  async deleteTranscript(id) {
    const response = await api.delete(`/transcripts/${id}`);
    return response.data;
  }

  async processTranscript(id) {
    const response = await api.post(`/transcripts/${id}/process`);
    return response.data;
  }

  async analyzeTranscript(id) {
    const response = await api.post(`/transcripts/${id}/analyze`);
    return response.data;
  }

  async extractRequirements(id) {
    const response = await api.post(`/transcripts/${id}/extract-requirements`);
    return response.data;
  }
}

export default new TranscriptService();
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\index.js
==================================================================

Chunk 1/1:
```
import { createPinia } from 'pinia';

const pinia = createPinia();

export default pinia;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\activity.js
=============================================================================

Chunk 1/1:
```
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useActivityStore = defineStore('activity', {
  state: () => ({
    activities: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchActivities() {
      try {
        this.loading = true;
        const response = await api.get('/activities');
        this.activities = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch activities';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\auth.js
=========================================================================

Chunk 1/1:
```
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token'),
    isAuthenticated: false,
    isLoading: false,
    error: null
  }),

  getters: {
    currentUser: (state) => state.user,
    isLoggedIn: (state) => state.isAuthenticated
  },

  actions: {
    async login(credentials) {
      try {
        this.isLoading = true;
        this.error = null;
        
        const response = await api.post('/auth/login', credentials);
        
        if (response.data.requiresTwoFactor) {
          return { requiresTwoFactor: true, tempToken: response.data.tempToken };
        }

        this.setAuthData(response.data);
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Login failed';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async verifyTwoFactor(data) {
      try {
        this.isLoading = true;
        this.error = null;
        
        const response = await api.post('/auth/verify-2fa', data);
        this.setAuthData(response.data);
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Verification failed';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async register(userData) {
      try {
        this.isLoading = true;
        this.error = null;
        
        const response = await api.post('/auth/register', userData);
        this.setAuthData(response.data);
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Registration failed';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async logout() {
      try {
        await api.post('/auth/logout');
      } catch (error) {
        console.error('Logout error:', error);
      } finally {
        this.clearAuthData();
      }
    },

    async refreshToken() {
      try {
        const response = await api.post('/auth/refresh');
        this.setAuthData(response.data);
        return response.data;
      } catch (error) {
        this.clearAuthData();
        throw error;
      }
    },

    async changePassword(passwordData) {
      try {
        this.isLoading = true;
        this.error = null;
        
        await api.post('/auth/change-password', passwordData);
      } catch (error) {
        this.error = error.response?.data?.message || 'Password change failed';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    setAuthData(data) {
      this.token = data.token;
      this.user = data.user;
      this.isAuthenticated = true;
      localStorage.setItem('token', data.token);
      api.defaults.headers.common['Authorization'] = `Bearer ${data.token}`;
    },

    clearAuthData() {
      this.token = null;
      this.user = null;
      this.isAuthenticated = false;
      localStorage.removeItem('token');
      delete api.defaults.headers.common['Authorization'];
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\gaps.js
=========================================================================

Chunk 1/1:
```
/* eslint-disable */
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useGapsStore = defineStore('gaps', {
  state: () => ({
    gaps: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchGaps() {
      try {
        this.loading = true;
        const response = await api.get('/gaps');
        this.gaps = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch gaps';
      } finally {
        this.loading = false;
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\notifications.js
==================================================================================

Chunk 1/1:
```
/* eslint-disable */
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useNotificationsStore = defineStore('notifications', {
  state: () => ({
    notifications: [],
    unreadCount: 0,
    loading: false,
    error: null
  }),

  getters: {
    hasUnread: (state) => state.unreadCount > 0
  },

  actions: {
    async fetchNotifications() {
      try {
        this.loading = true;
        const response = await api.get('/notifications');
        this.notifications = response.data;
        this.unreadCount = this.notifications.filter(n => !n.read).length;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch notifications';
      } finally {
        this.loading = false;
      }
    },

    async markAsRead(id) {
      try {
        await api.put(`/notifications/${id}/read`);
        const notification = this.notifications.find(n => n.id === id);
        if (notification && !notification.read) {
          notification.read = true;
          this.unreadCount--;
        }
      } catch (error) {
        console.error('Failed to mark notification as read:', error);
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\requirements.js
=================================================================================

Chunk 1/1:
```
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useRequirementsStore = defineStore('requirements', {
  state: () => ({
    requirements: [],
    currentRequirement: null,
    isLoading: false,
    error: null
  }),

  getters: {
    getRequirementById: (state) => (id) => {
      return state.requirements.find(r => r.RequirementID === id);
    },

    requirementsByStatus: (state) => (status) => {
      return state.requirements.filter(r => r.Status === status);
    }
  },

  actions: {
    async fetchRequirements() {
      try {
        this.isLoading = true;
        const response = await api.get('/requirements');
        this.requirements = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch requirements';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async fetchRequirementById(id) {
      try {
        this.isLoading = true;
        const response = await api.get(`/requirements/${id}`);
        this.currentRequirement = response.data;
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch requirement';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async createRequirement(data) {
      try {
        this.isLoading = true;
        const response = await api.post('/requirements', data);
        this.requirements.push(response.data);
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to create requirement';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async updateRequirement(id, data) {
      try {
        this.isLoading = true;
        const response = await api.put(`/requirements/${id}`, data);
        const index = this.requirements.findIndex(r => r.RequirementID === id);
        if (index !== -1) {
          this.requirements[index] = response.data;
        }
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to update requirement';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async deleteRequirement(id) {
      try {
        this.isLoading = true;
        await api.delete(`/requirements/${id}`);
        this.requirements = this.requirements.filter(r => r.RequirementID !== id);
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to delete requirement';
        throw error;
      } finally {
        this.isLoading = false;
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\stakeholders.js
=================================================================================

Chunk 1/2:
```
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useStakeholdersStore = defineStore('stakeholders', {
  state: () => ({
    stakeholders: [],
    currentStakeholder: null,
    isLoading: false,
    error: null
  }),

  getters: {
    getStakeholderById: (state) => (id) => {
      return state.stakeholders.find(s => s.StakeholderID === id);
    },

    stakeholdersByRole: (state) => (role) => {
      return state.stakeholders.filter(s => s.StakeholderRole === role);
    },

    stakeholdersByInfluence: (state) => (level) => {
      return state.stakeholders.filter(s => s.InfluenceLevel === level);
    }
  },

  actions: {
    async fetchStakeholders() {
      try {
        this.isLoading = true;
        const response = await api.get('/stakeholders');
        this.stakeholders = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch stakeholders';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async fetchStakeholderById(id) {
      try {
        this.isLoading = true;
        const response = await api.get(`/stakeholders/${id}`);
        this.currentStakeholder = response.data;
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch stakeholder';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async createStakeholder(data) {
      try {
        this.isLoading = true;
        const response = await api.post('/stakeholders', data);
        this.stakeholders.push(response.data);
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to create stakeholder';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async updateStakeholder(id, data) {
      try {
        this.isLoading = true;
        const response = await api.put(`/stakeholders/${id}`, data);
        const index = this.stakeholders.findIndex(s => s.StakeholderID === id);
        if (index !== -1) {
          this.stakeholders[index] = response.data;
        }
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to update stakeholder';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async deleteStakeholder(id) {
      try {
        this.isLoading = true;
        await api.delete(`/stakeholders/${id}`);
        this.stakeholders = this.stakeholders.filter(s => s.StakeholderID !== id);
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to delete stakeholder';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async importStakeholders(file) {
      try {
        this.isLoading = true;
        const formData = new FormData();
        formData.append('file', file);
        const response = await api.post('/stakeholders/import', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.stakeholders = [...this.stakeholders, ...response.data];
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to import stakeholders';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async exportToExcel() {
      try {
        this.isLoading = true;
        const response = await api.get('/stakeholders/export', {
          responseType: 'blob'
        });
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'stakeholders.xlsx');
        document.body.appendChild(link);
        link.click();
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to exp
```


Chunk 2/2:
```
ort stakeholders';
        throw error;
      } finally {
        this.isLoading = false;
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\transcripts.js
================================================================================

Chunk 1/1:
```
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useTranscriptsStore = defineStore('transcripts', {
  state: () => ({
    transcripts: [],
    currentTranscript: null,
    isLoading: false,
    error: null
  }),

  getters: {
    getTranscriptById: (state) => (id) => {
      return state.transcripts.find(t => t.TranscriptID === id);
    }
  },

  actions: {
    async fetchTranscripts() {
      try {
        this.isLoading = true;
        const response = await api.get('/transcripts');
        this.transcripts = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch transcripts';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async fetchTranscriptById(id) {
      try {
        this.isLoading = true;
        const response = await api.get(`/transcripts/${id}`);
        this.currentTranscript = response.data;
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch transcript';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async createTranscript(data) {
      try {
        this.isLoading = true;
        const response = await api.post('/transcripts', data);
        this.transcripts.push(response.data);
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to create transcript';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async updateTranscript(id, data) {
      try {
        this.isLoading = true;
        const response = await api.put(`/transcripts/${id}`, data);
        const index = this.transcripts.findIndex(t => t.TranscriptID === id);
        if (index !== -1) {
          this.transcripts[index] = response.data;
        }
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to update transcript';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async deleteTranscript(id) {
      try {
        this.isLoading = true;
        await api.delete(`/transcripts/${id}`);
        this.transcripts = this.transcripts.filter(t => t.TranscriptID !== id);
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to delete transcript';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async processTranscript(id) {
      try {
        this.isLoading = true;
        const response = await api.post(`/transcripts/${id}/process`);
        const index = this.transcripts.findIndex(t => t.TranscriptID === id);
        if (index !== -1) {
          this.transcripts[index] = response.data;
        }
        return response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to process transcript';
        throw error;
      } finally {
        this.isLoading = false;
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\store\modules\user.js
=========================================================================

Chunk 1/1:
```
import { defineStore } from 'pinia';
import api from '@/services/api';

export const useUserStore = defineStore('user', {
  state: () => ({
    profile: null,
    loading: false,
    error: null
  }),

  actions: {
    async fetchProfile() {
      try {
        this.loading = true;
        const response = await api.get('/user/profile');
        this.profile = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to fetch profile';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateProfile(data) {
      try {
        this.loading = true;
        const response = await api.put('/user/profile', data);
        this.profile = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Failed to update profile';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\utils\formatters.js
=======================================================================

Chunk 1/2:
```
import { format, parseISO, formatDistance, formatRelative } from 'date-fns';

/**
 * Date formatters
 */
export const dateFormatters = {
  /**
   * Format date to standard display format
   * @param {string|Date} date - Date to format
   * @param {string} formatStr - Optional format string
   * @returns {string} Formatted date
   */
  formatDate(date, formatStr = 'MMM d, yyyy') {
    if (!date) return '';
    try {
      const dateObj = typeof date === 'string' ? parseISO(date) : date;
      return format(dateObj, formatStr);
    } catch (error) {
      console.error('Date formatting error:', error);
      return date;
    }
  },

  /**
   * Format date and time
   * @param {string|Date} date - Date to format
   * @returns {string} Formatted date and time
   */
  formatDateTime(date) {
    return this.formatDate(date, 'MMM d, yyyy h:mm a');
  },

  /**
   * Get relative time (e.g., "2 hours ago")
   * @param {string|Date} date - Date to format
   * @returns {string} Relative time
   */
  getRelativeTime(date) {
    if (!date) return '';
    try {
      const dateObj = typeof date === 'string' ? parseISO(date) : date;
      return formatDistance(dateObj, new Date(), { addSuffix: true });
    } catch (error) {
      console.error('Relative time formatting error:', error);
      return date;
    }
  },

  /**
   * Get relative calendar time (e.g., "yesterday at 2:30 PM")
   * @param {string|Date} date - Date to format
   * @returns {string} Relative calendar time
   */
  getRelativeCalendar(date) {
    if (!date) return '';
    try {
      const dateObj = typeof date === 'string' ? parseISO(date) : date;
      return formatRelative(dateObj, new Date());
    } catch (error) {
      console.error('Relative calendar formatting error:', error);
      return date;
    }
  }
};

/**
 * Number formatters
 */
export const numberFormatters = {
  /**
   * Format number with comma separators
   * @param {number} number - Number to format
   * @returns {string} Formatted number
   */
  formatNumber(number) {
    return new Intl.NumberFormat().format(number);
  },

  /**
   * Format file size
   * @param {number} bytes - Size in bytes
   * @returns {string} Formatted file size
   */
  formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  },

  /**
   * Format duration in minutes to hours and minutes
   * @param {number} minutes - Duration in minutes
   * @returns {string} Formatted duration
   */
  formatDuration(minutes) {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    if (hours === 0) return `${mins}m`;
    return `${hours}h ${mins}m`;
  },

  /**
   * Format percentage
   * @param {number} value - Value to format
   * @param {number} decimals - Number of decimal places
   * @returns {string} Formatted percentage
   */
  formatPercentage(value, decimals = 1) {
    return `${value.toFixed(decimals)}%`;
  }
};

/**
 * Text formatters
 */
export const textFormatters = {
  /**
   * Capitalize first letter of each word
   * @param {string} text - Text to format
   * @returns {string} Formatted text
   */
  capitalizeWords(text) {
    if (!text) return '';
    return text.replace(/\b\w/g, l => l.toUpperCase());
  },

  /**
   * Truncate text with ellipsis
   * @param {string} text - Text to truncate
   * @param {number} length - Maximum length
   * @returns {string} Truncated text
   */
  truncateText(text, length = 50) {
    if (!text) return '';
    if (text.length <= length) return text;
    return text.substring(0, length) + '...';
  },

  /**
   * Format name initials
   * @param {string} name - Full name
   * @returns {string} Initials
   */
  getInitials(name) {
    if (!name) return '';
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase();
  },

  /**
  
```


Chunk 2/2:
```
 * Convert snake_case to Title Case
   * @param {string} text - Text to format
   * @returns {string} Formatted text
   */
  snakeToTitleCase(text) {
    if (!text) return '';
    return text
      .split('_')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
      .join(' ');
  }
};

export default {
  ...dateFormatters,
  ...numberFormatters,
  ...textFormatters
};
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\utils\notifications.js
==========================================================================

Chunk 1/1:
```
import { createApp } from 'vue';
import { createVuetify } from 'vuetify';

const vuetify = createVuetify();

/**
 * Notification types
 */
export const NotificationType = {
  SUCCESS: 'success',
  ERROR: 'error',
  WARNING: 'warning',
  INFO: 'info'
};

/**
 * Notification manager class
 */
class NotificationManager {
  constructor() {
    this.queue = [];
    this.isProcessing = false;
    this.snackbar = null;
  }

  /**
   * Initialize notification manager
   */
  init() {
    // Create snackbar component
    const SnackbarComponent = {
      data() {
        return {
          show: false,
          message: '',
          color: '',
          timeout: 3000
        };
      },
      template: `
        <v-snackbar
          v-model="show"
          :color="color"
          :timeout="timeout"
          location="top"
        >
          {{ message }}
          <template v-slot:actions>
            <v-btn
              variant="text"
              @click="show = false"
            >
              Close
            </v-btn>
          </template>
        </v-snackbar>
      `
    };

    // Mount snackbar
    const app = createApp(SnackbarComponent);
    app.use(vuetify);
    
    const snackbarElement = document.createElement('div');
    document.body.appendChild(snackbarElement);
    this.snackbar = app.mount(snackbarElement);
  }

  /**
   * Show notification
   * @param {string} message - Notification message
   * @param {string} type - Notification type
   * @param {number} timeout - Display duration in milliseconds
   */
  show(message, type = NotificationType.INFO, timeout = 3000) {
    this.queue.push({ message, type, timeout });
    this.processQueue();
  }

  /**
   * Process notification queue
   */
  async processQueue() {
    if (this.isProcessing || this.queue.length === 0) return;

    this.isProcessing = true;
    const { message, type, timeout } = this.queue.shift();

    this.snackbar.message = message;
    this.snackbar.color = type;
    this.snackbar.timeout = timeout;
    this.snackbar.show = true;

    await new Promise(resolve => setTimeout(resolve, timeout));
    this.isProcessing = false;
    this.processQueue();
  }

  /**
   * Show success notification
   * @param {string} message - Success message
   * @param {number} timeout - Display duration in milliseconds
   */
  success(message, timeout = 3000) {
    this.show(message, NotificationType.SUCCESS, timeout);
  }

  /**
   * Show error notification
   * @param {string} message - Error message
   * @param {number} timeout - Display duration in milliseconds
   */
  error(message, timeout = 5000) {
    this.show(message, NotificationType.ERROR, timeout);
  }

  /**
   * Show warning notification
   * @param {string} message - Warning message
   * @param {number} timeout - Display duration in milliseconds
   */
  warning(message, timeout = 4000) {
    this.show(message, NotificationType.WARNING, timeout);
  }

  /**
   * Show info notification
   * @param {string} message - Info message
   * @param {number} timeout - Display duration in milliseconds
   */
  info(message, timeout = 3000) {
    this.show(message, NotificationType.INFO, timeout);
  }
}

export const notifications = new NotificationManager();

export default notifications;
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\utils\validators.js
=======================================================================

Chunk 1/1:
```
/**
 * Form validators
 */
export const formValidators = {
    /**
     * Required field validator
     * @param {any} value - Field value
     * @returns {boolean|string} True if valid, error message if invalid
     */
    required(value) {
      return !!value || 'This field is required';
    },
  
    /**
     * Email validator
     * @param {string} email - Email to validate
     * @returns {boolean|string} True if valid, error message if invalid
     */
    email(email) {
      const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return pattern.test(email) || 'Invalid email address';
    },
  
    /**
     * Password validator
     * @param {string} password - Password to validate
     * @returns {boolean|string} True if valid, error message if invalid
     */
    password(password) {
      const minLength = 8;
      const hasUpperCase = /[A-Z]/.test(password);
      const hasLowerCase = /[a-z]/.test(password);
      const hasNumbers = /\d/.test(password);
      const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  
      if (password.length < minLength) return 'Password must be at least 8 characters';
      if (!hasUpperCase) return 'Password must contain at least one uppercase letter';
      if (!hasLowerCase) return 'Password must contain at least one lowercase letter';
      if (!hasNumbers) return 'Password must contain at least one number';
      if (!hasSpecialChar) return 'Password must contain at least one special character';
  
      return true;
    },
  
    /**
     * Phone number validator
     * @param {string} phone - Phone number to validate
     * @returns {boolean|string} True if valid, error message if invalid
     */
    phone(phone) {
      const pattern = /^\+?[1-9]\d{1,14}$/;
      return pattern.test(phone) || 'Invalid phone number';
    },
  
    /**
     * URL validator
     * @param {string} url - URL to validate
     * @returns {boolean|string} True if valid, error message if invalid
     */
    url(url) {
      try {
        new URL(url);
        return true;
      } catch {
        return 'Invalid URL';
      }
    }
  };
  
  /**
   * Data validators
   */
  export const dataValidators = {
    /**
     * Validate requirement data
     * @param {Object} requirement - Requirement data
     * @returns {Object} Validation result
     */
    validateRequirement(requirement) {
      const errors = {};
  
      if (!requirement.RequirementTitle) {
        errors.title = 'Title is required';
      }
  
      if (!requirement.RequirementType) {
        errors.type = 'Type is required';
      }
  
      if (!requirement.Priority) {
        errors.priority = 'Priority is required';
      }
  
      return {
        isValid: Object.keys(errors).length === 0,
        errors
      };
    },
  
    /**
     * Validate stakeholder data
     * @param {Object} stakeholder - Stakeholder data
     * @returns {Object} Validation result
     */
    validateStakeholder(stakeholder) {
      const errors = {};
  
      if (!stakeholder.StakeholderName) {
        errors.name = 'Name is required';
      }
  
      if (stakeholder.ContactInformation && !formValidators.email(stakeholder.ContactInformation)) {
        errors.email = 'Invalid email address';
      }
  
      return {
        isValid: Object.keys(errors).length === 0,
        errors
      };
    }
  };
  
  export default {
    ...formValidators,
    ...dataValidators
  };
```

--------------------------------------------------------------------------------

File: ../InstAanlyst-AI/InstAnalyst-AI\frontend\src\assets\css\main.css
=======================================================================

Chunk 1/1:
```
/* Global styles */
* {
    box-sizing: border-box;
  }
  
  body {
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f7fa;
    color: #333;
    line-height: 1.6;
  }
  
  h1, h2, h3, h4, h5, h6 {
    margin-top: 0;
    color: #2c3e50;
  }
  
  a {
    color: #3498db;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  button {
    cursor: pointer;
  }
  
  button:disabled {
    cursor: not-allowed;
    opacity: 0.6;
  }
  
  /* Utility classes */
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }
  
  .text-center {
    text-align: center;
  }
  
  .text-error {
    color: #e74c3c;
  }
  
  .text-success {
    color: #2ecc71;
  }
  
  .text-warning {
    color: #f39c12;
  }
  
  /* Responsive breakpoints */
  @media (max-width: 576px) {
    .hide-sm {
      display: none;
    }
  }
  
  @media (max-width: 768px) {
    .hide-md {
      display: none;
    }
  }
  
  @media (max-width: 992px) {
    .hide-lg {
      display: none;
    }
  }
```

--------------------------------------------------------------------------------


4. Specific issues I'm aware of:
the requirements need to save to the database

5. Priority areas:
remove login feature
