import { execSync } from 'child_process'
import path from 'path'

export function getGitFileCreationDate(filePath) {
  try {
    // Extract file name from path
    const fileName = path.basename(filePath);

    // Use case-insensitive search for the file name
    const cmd = `git log --diff-filter=A --format=%at -- "*${fileName}"`
    const timestamp = execSync(cmd, { encoding: 'utf-8' }).trim();

    if (!timestamp) {
      // No git creation date found (probably a non-committed new file)
      // The date will appear in the next build
      return null;
    }

    // Convert git timestamp to Date
    return new Date(parseInt(timestamp) * 1000);
  } catch (e) {
    console.error(`Failed to get git creation date for ${filePath}:`, e);
    return null;
  }
}
